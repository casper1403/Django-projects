# Generated by Django 3.0.7 on 2020-06-23 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_auto_20200622_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='points',
            field=models.IntegerField(blank=True),
        ),
    ]
