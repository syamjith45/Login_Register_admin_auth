# Generated by Django 4.2.8 on 2023-12-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the product name', max_length=255)),
                ('category', models.CharField(choices=[('sports', 'Sports Equipment'), ('clothing', 'Sportswear')], help_text='Select the product category', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, help_text='Enter the product price', max_digits=10)),
                ('stock', models.PositiveIntegerField(help_text='Enter the product stock')),
                ('image', models.ImageField(blank=True, help_text='Upload product image', null=True, upload_to='product_images/')),
            ],
        ),
    ]
