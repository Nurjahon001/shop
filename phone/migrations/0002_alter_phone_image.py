# Generated by Django 5.0.1 on 2024-01-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
