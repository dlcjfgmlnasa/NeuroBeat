# -*- coding:utf-8 -*-
import numpy as np
from scipy import fftpack
from scipy.signal import butter, lfilter


def butter_bandpass_filter(data, lowcut, highcut, sfreq, order=5):
    nyq = 0.5 * sfreq
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = lfilter(b, a, data)
    return y


class FastFourierTransform(object):
    def __init__(self, data, sfreq):
        self.data = data
        self.sfreq = sfreq

    def psd(self):
        samples = self.data.shape[0]
        frequencies = fftpack.fftfreq(samples) * self.sfreq
        psd = abs(fftpack.fft(self.data) / samples)
        return frequencies, psd

    def absolute_power(self):
        frequencies, psd = self.psd()

        # Find intersecting values in frequency vector
        delta_idx = np.where(np.logical_and(1 <= frequencies, frequencies < 4))[0]
        theta_idx = np.where(np.logical_and(4 <= frequencies, frequencies < 8))[0]
        low_alpha_idx = np.where(np.logical_and(8 <= frequencies, frequencies < 10))[0]
        high_alpha_idx = np.where(np.logical_and(10 <= frequencies, frequencies < 12))[0]
        low_beta_idx = np.where(np.logical_and(12 <= frequencies, frequencies < 16))[0]
        high_beta_idx = np.where(np.logical_and(16 <= frequencies, frequencies < 32))[0]
        gamma_idx = np.where(np.logical_and(32 <= frequencies, frequencies < 60))[0]

        # Absolute power
        absolute_delta = np.sum(psd[delta_idx, :], axis=0)
        absolute_theta = np.sum(psd[theta_idx, :], axis=0)
        absolute_low_alpha = np.sum(psd[low_alpha_idx, :], axis=0)
        absolute_high_alpha = np.sum(psd[high_alpha_idx, :], axis=0)
        absolute_low_beta = np.sum(psd[low_beta_idx, :], axis=0)
        absolute_high_beta = np.sum(psd[high_beta_idx, :], axis=0)
        absolute_gamma = np.sum(psd[gamma_idx, :], axis=0)
        return absolute_delta, absolute_theta, absolute_low_alpha, absolute_high_alpha, absolute_low_beta, \
               absolute_high_beta, absolute_gamma

    def relative_power(self):
        absolute_delta, absolute_theta, absolute_low_alpha, absolute_high_alpha, absolute_low_beta, \
        absolute_high_beta, absolute_gamma = self.absolute_power()
        # Relative power
        total_power = absolute_delta + absolute_theta + absolute_low_alpha + absolute_high_alpha + \
                      absolute_low_beta + absolute_high_beta + absolute_gamma
        relative_delta = absolute_delta / total_power
        relative_theta = absolute_theta / total_power
        relative_low_alpha = absolute_low_alpha / total_power
        relative_high_alpha = absolute_high_alpha / total_power
        relative_low_beta = absolute_low_beta / total_power
        relative_high_beta = absolute_high_beta / total_power
        relative_gamma = absolute_gamma / total_power
        return relative_delta, relative_theta, relative_low_alpha, relative_high_alpha, relative_low_beta, \
               relative_high_beta, relative_gamma


def attention(data, sfreq):
    """
    Estimate attention level
    Params:
      data: ndarray, shape (n_times, n_channels)
        The data to estimate attention.
      sfreq: int
        The sample frequency in Hz.
    Return:
      attention_level: ndarray, shape (n_times, n_channels)
        The estimated attention level.
    """
    # Band-pass filter 0.1-60 Hz
    # filtered_data = butter_bandpass_filter(data, lowcut=0.1, highcut=60, sfreq=sfreq)
    fft = FastFourierTransform(data, sfreq)
    _, relative_theta, relative_low_alpha, relative_high_alpha, relative_low_beta, _, _ = fft.relative_power()
    attention_level = (relative_low_beta.mean()+relative_high_alpha.mean()) / \
                      (relative_low_alpha.mean() + relative_theta.mean())
    return attention_level
