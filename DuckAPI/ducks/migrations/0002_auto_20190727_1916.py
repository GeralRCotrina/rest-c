# Generated by Django 2.2.3 on 2019-07-28 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ducks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duck',
            old_name='duckmail',
            new_name='duckemail',
        ),
    ]
