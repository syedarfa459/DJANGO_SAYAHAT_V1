# Generated by Django 3.1.2 on 2021-03-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdventureClub', '0005_auto_20210301_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adventureevent',
            name='event_by',
            field=models.CharField(max_length=100),
        ),
    ]