# Generated by Django 4.2.9 on 2024-09-16 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodact_categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categori_name', models.CharField(max_length=12)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('isActive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Prodact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodact_name', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('technical_specifications', models.TextField(max_length=150)),
                ('images', models.ImageField(upload_to='')),
                ('isActive', models.BooleanField()),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('prodact_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.prodact_categories')),
            ],
        ),
    ]
