# Generated by Django 4.1.2 on 2022-10-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeddyBear', '0005_alter_products_amount_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
