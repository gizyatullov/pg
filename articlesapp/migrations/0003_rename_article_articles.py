# Generated by Django 4.0.4 on 2022-05-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articlesapp', '0002_alter_topic_is_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Articles',
        ),
    ]
