# Generated by Django 2.1.7 on 2019-03-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_models', '0009_auto_20190320_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]
