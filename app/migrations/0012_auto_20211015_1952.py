# Generated by Django 3.2.8 on 2021-10-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20211015_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='real_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='value',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
