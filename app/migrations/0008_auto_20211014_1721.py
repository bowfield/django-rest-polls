# Generated by Django 3.2.8 on 2021-10-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_poll_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='poll',
            name='type',
            field=models.CharField(default='', max_length=10),
        ),
    ]
