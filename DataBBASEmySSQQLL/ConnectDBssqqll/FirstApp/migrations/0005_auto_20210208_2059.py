# Generated by Django 3.1.4 on 2021-02-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0004_oeecalculations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oeecalculations',
            name='A',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='oeecalculations',
            name='OEE',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='oeecalculations',
            name='P',
            field=models.IntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='oeecalculations',
            name='Q',
            field=models.IntegerField(max_length=3),
        ),
    ]
