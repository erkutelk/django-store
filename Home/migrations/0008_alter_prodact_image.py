# Generated by Django 4.2.9 on 2024-09-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_uploadmodel_alter_prodact_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodact',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
