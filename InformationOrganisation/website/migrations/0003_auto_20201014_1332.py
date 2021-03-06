# Generated by Django 3.1.2 on 2020-10-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201014_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='authors',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='isbn',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='original_publication_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='original_title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
