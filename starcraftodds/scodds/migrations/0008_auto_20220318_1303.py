# Generated by Django 2.2.15 on 2022-03-18 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scodds', '0007_matchup_kellyvalue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchup',
            old_name='KellyValue',
            new_name='kellyValue',
        ),
    ]
