# Generated by Django 5.0 on 2023-12-05 15:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cateogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Cateogory',
                'verbose_name_plural': 'Cateogories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cateogory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cateogory', verbose_name='category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product', verbose_name='oroduct')),
            ],
            options={
                'verbose_name': 'ProductCategory',
                'verbose_name_plural': 'ProductCategorys',
            },
        ),
    ]