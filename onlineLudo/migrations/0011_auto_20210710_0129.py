# Generated by Django 3.2.4 on 2021-07-09 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlineLudo', '0010_onlineplayer_needsteps'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onlineplayer',
            old_name='needsteps',
            new_name='updateGame',
        ),
        migrations.RenameField(
            model_name='onlineplayer',
            old_name='update',
            new_name='updateMessage',
        ),
    ]
