# Generated by Django 3.0.7 on 2020-06-25 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0009_auto_20200623_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='trainer',
        ),
        migrations.AddField(
            model_name='profile',
            name='pokemon',
            field=models.ManyToManyField(to='trainer.Pokemon'),
        ),
    ]