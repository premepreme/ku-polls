# Generated by Django 4.1 on 2022-09-23 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
    ]