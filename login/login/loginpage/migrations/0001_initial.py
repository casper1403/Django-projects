# Generated by Django 3.0.3 on 2020-02-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Typenummer', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('Lijn', models.CharField(max_length=20)),
                ('Categorie', models.CharField(max_length=60)),
                ('kW', models.CharField(max_length=20)),
                ('Voltage', models.CharField(max_length=20)),
                ('Afmetingen', models.CharField(max_length=30)),
                ('Aansluiting', models.CharField(max_length=30)),
                ('Inhoud', models.CharField(max_length=30)),
                ('Prijs', models.IntegerField(default=0)),
                ('extra', models.CharField(max_length=500)),
            ],
        ),
    ]