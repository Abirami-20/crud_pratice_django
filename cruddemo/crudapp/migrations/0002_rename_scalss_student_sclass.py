# Generated by Django 5.0 on 2024-01-10 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='scalss',
            new_name='sclass',
        ),
    ]
