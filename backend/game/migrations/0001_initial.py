# Generated by Django 4.0.5 on 2022-11-08 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('neuro_feedback', models.BooleanField(db_column='NEURO_FEEDBACK_FLAG')),
                ('binaural_beats', models.BooleanField(db_column='BINAURAL_BEATS_FLAG')),
                ('speed', models.FloatField(db_column='SPEED')),
                ('rank', models.CharField(choices=[(1, 'S'), (2, 'A'), (3, 'B'), (4, 'C'), (5, 'D'), (6, 'F')], db_column='RANK', max_length=4)),
                ('score', models.IntegerField(db_column='SCORE')),
                ('rhythm_score', models.IntegerField(db_column='RHYTHM_SCORE')),
                ('memory_score', models.IntegerField(db_column='MEMORY_SCORE')),
                ('color_score', models.IntegerField(db_column='COLOR_SCORE')),
                ('rhythm_score_great_count', models.IntegerField(db_column='RHYTHM_SCORE_GREAT_COUNT')),
                ('rhythm_score_good_count', models.IntegerField(db_column='RHYTHM_SCORE_GOOD_COUNT')),
                ('rhythm_score_bad_count', models.IntegerField(db_column='RHYTHM_SCORE_BAD_COUNT')),
                ('rhythm_score_miss_count', models.IntegerField(db_column='RHYTHM_SCORE_MISS_COUNT')),
                ('memory_score_great_count', models.IntegerField(db_column='MEMORY_SCORE_GREAT_COUNT')),
                ('memory_score_good_count', models.IntegerField(db_column='MEMORY_SCORE_GOOD_COUNT')),
                ('memory_score_bad_count', models.IntegerField(db_column='MEMORY_SCORE_BAD_COUNT')),
                ('memory_score_miss_count', models.IntegerField(db_column='MEMORY_SCORE_MISS_COUNT')),
                ('color_score_great_count', models.IntegerField(db_column='COLOR_SCORE_GREAT_COUNT')),
                ('color_score_good_count', models.IntegerField(db_column='COLOR_SCORE_GOOD_COUNT')),
                ('color_score_bad_count', models.IntegerField(db_column='COLOR_SCORE_BAD_COUNT')),
                ('color_score_miss_count', models.IntegerField(db_column='COLOR_SCORE_MISS_COUNT')),
                ('max_combo', models.IntegerField(db_column='MAX_COMBO')),
                ('focused', models.IntegerField(db_column='FOCUSED')),
                ('attention', models.FloatField(db_column='ATTENTION')),
            ],
            options={
                'db_table': 'NG_GAME',
            },
        ),
        migrations.CreateModel(
            name='MiniGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('game_type', models.CharField(choices=[(1, 'Corsi Block Test'), (2, 'Digit Span Test'), (3, 'K-TMT-E'), (4, 'K-BNT'), (5, 'SVLT-E')], db_column='MINI_GAME_TYPE', max_length=30)),
                ('score', models.IntegerField(db_column='SCORE')),
            ],
            options={
                'db_table': 'NG_MINI_GAME',
            },
        ),
    ]
