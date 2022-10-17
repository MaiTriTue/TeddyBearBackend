from rest_framework.serializers import ModelSerializer
from .models import *


class ProductSerialize(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'name', 'image', 'discription', 'type', 'color',
                  'size', 'material', 'amount_sold', 'price', 'tags', 'category']
