# Generated by Django 2.2.15 on 2022-03-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scodds', '0005_matchup_best_of'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='p1AligulacOdds',
            field=models.IntegerField(default=0),
        ),
    ]
