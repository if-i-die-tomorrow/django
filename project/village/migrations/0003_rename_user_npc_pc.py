# Generated by Django 4.2.1 on 2023-06-03 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0002_alter_npc_pronouns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='npc',
            old_name='user',
            new_name='pc',
        ),
    ]