# Generated by Django 3.2.11 on 2023-07-20 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_validator', '0005_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='creator',
        ),
        migrations.DeleteModel(
            name='Favourites',
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.DeleteModel(
            name='Podcast',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
