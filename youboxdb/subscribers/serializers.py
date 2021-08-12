from rest_framework import serializers
from .models import *
# from djoser.serializers import UserCreateSerializer, UserSerializer


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'type']


#Use to Post,Put or Delete
class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'street_address', 'city', 'state', 'zip_code', 'phone']


#use on get request
class UtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utoken
        fields = ['id', 'user_id']


#Use to Post,Put or Delete
class PostUtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utoken
        fields = ['id', 'user_id']


#use on get request
class UserSerializer(serializers.ModelSerializer):
    token = UtokenSerializer(read_only=True)#includes upgrade tokens on get

    class Meta:
        model = User
        fields = ['id', 'role', 'email', 'street_address', 'city', 'state', 'zip_code', 'phone']


#Use to Post,Put or Delete
class PostClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['id', 'image_id', 'user_id', 'city', 'type', 'brand', 'style', 'material', 'pattern', 'size', 'color']


#use on get request
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user_id', 'item_id', 'image']


#use on post, put or delete
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user_id', 'item_id', 'image']


#use on get request
class ClothingSerializer(serializers.ModelSerializer):
    image = ImageSerializer(read_only=True)#includes image on get

    class Meta:
        model = Clothing
        fields = ['id', 'image_id', 'user_id', 'city', 'type', 'brand', 'style', 'material', 'pattern', 'size', 'color']


#use on get request
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user_id', 'name', 'number_items', 'price', 'delivery_freq']


#Use to Post,Put or Delete
class PostSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user_id', 'name', 'number_items', 'price', 'delivery_freq']


#use on get request
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) #includes user on get
    subscription = SubscriptionSerializer(read_only=True)#includes subscription on get
    clothing = ClothingSerializer(read_only=True, many=True)#includes all clothing in get

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'subscription_id', 'clothing_items', 'total', 'est_delivery']


#Use to Post,Put or Delete
class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_id', 'subscription_id', 'clothing_items', 'total', 'est_delivery']


