# Generated by Django 2.2.15 on 2022-03-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scodds', '0004_auto_20210425_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='best_of',
            field=models.IntegerField(default=3),
        ),
    ]