# Generated by Django 3.0.3 on 2020-02-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Voltage',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='extra',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='kW',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
