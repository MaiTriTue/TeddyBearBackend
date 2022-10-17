from email.policy import default
from django.db import models

# Create your models here.


class ItemBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(null=False, max_length=255, unique=True)
    image = models.CharField(null=False, max_length=500, unique=True)
    # image = models.ImageField(upload_to='products/%Y/%m', default=None)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Discount(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(null=False, max_length=255, unique=True)

    def __str__(self):
        return self.name


class Products(ItemBase):
    class Meta:
        ordering = ['id']
        unique_together = ('name', 'category')
    discription = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True)
    color = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True)
    material = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    like = models.IntegerField(null=True, blank=True)
    amount_sold = models.IntegerField(null=True, blank=True, default=0)

    tags = models.ManyToManyField(
        'Discount', blank=True, null=True, related_name='discoumt')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
