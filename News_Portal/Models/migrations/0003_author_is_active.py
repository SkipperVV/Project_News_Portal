# Generated by Django 4.2.4 on 2024-01-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_comment_text_en_us_comment_text_ru_post_text_en_us_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]