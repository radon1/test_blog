# Generated by Django 2.1.7 on 2019-04-11 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_models', '0011_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=55, verbose_name='Url'),
        ),
    ]
