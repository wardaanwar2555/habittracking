# Generated by Django 5.1.5 on 2025-02-20 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0004_ab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ab',
            old_name='habit_name',
            new_name='name',
        ),
    ]
