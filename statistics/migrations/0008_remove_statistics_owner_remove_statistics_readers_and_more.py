# Generated by Django 4.1.5 on 2023-01-25 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0007_alter_userstatisticsrelation_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statistics',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='readers',
        ),
        migrations.DeleteModel(
            name='UserStatisticsRelation',
        ),
    ]