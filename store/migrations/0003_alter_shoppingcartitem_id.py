# Generated by Django 4.0.3 on 2022-03-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
