# Generated by Django 2.2.15 on 2022-07-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scodds', '0015_auto_20220728_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='age',
            field=models.FloatField(default=0),
        ),
    ]
