# Generated by Django 4.0.5 on 2022-11-16 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0003_alter_minigame_game_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BioSignal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('device_type', models.CharField(choices=[(1, 'neurotx')], default='neurotx', max_length=20)),
                ('game', models.ForeignKey(db_column='GAME_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='signal', to='game.game')),
            ],
            options={
                'db_table': 'NG_BIO_SIGNAL',
            },
        ),
    ]
