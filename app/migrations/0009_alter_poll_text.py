# Generated by Django 3.2.8 on 2021-10-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211014_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.CharField(default='', max_length=30),
        ),
    ]
