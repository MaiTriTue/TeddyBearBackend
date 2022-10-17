# Generated by Django 4.1.2 on 2022-10-14 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeddyBear', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='products/%Y/%m')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('color', models.CharField(max_length=255, null=True)),
                ('size', models.CharField(max_length=255, null=True)),
                ('material', models.CharField(max_length=255, null=True)),
                ('price', models.CharField(max_length=255, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('amount_sold', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TeddyBear.category')),
                ('tags', models.ManyToManyField(blank=True, null=True, related_name='discoumt', to='TeddyBear.discount')),
            ],
            options={
                'unique_together': {('name', 'category')},
            },
        ),
    ]
