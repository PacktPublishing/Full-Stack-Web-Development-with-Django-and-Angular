from django.contrib.auth.models import User
from .models import Product
from rest_framework import serializers

# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ['name', 'price', 'currency']
        fields = '__all__'