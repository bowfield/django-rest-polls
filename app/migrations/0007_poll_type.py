# Generated by Django 3.2.8 on 2021-10-14 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_pollanswer_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='type',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]