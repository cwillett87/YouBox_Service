from rest_framework import serializers
from .models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'type']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'street_address', 'city', 'state', 'zip_code', 'phone']


class UtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utoken
        fields = ['id', 'user_id']


class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['id', 'image_id', 'user_id', 'city', 'type', 'brand', 'style', 'material', 'pattern', 'size', 'color']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user_id', 'item_id', 'image']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user_id', 'name', 'number_items', 'price', 'delivery_freq']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'subscription_id', 'clothing_items', 'total', 'est_delivery']


