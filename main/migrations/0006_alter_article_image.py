# Generated by Django 5.1.6 on 2025-03-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_article_public_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
