# Generated by Django 3.0.4 on 2020-03-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200319_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toy',
            name='color',
            field=models.CharField(max_length=20),
        ),
    ]
