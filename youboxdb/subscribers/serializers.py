from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'type']


#Use to Post,Put or Delete
class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'image_Id', 'email', 'street_Address', 'city', 'state', 'zip_Code', 'phone']


#use on get request
class UtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utoken
        fields = ['id', 'user_Id']


#Use to Post,Put or Delete
class PostUtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utoken
        fields = ['id', 'user_Id']


#use on get request
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user_Id', 'item_Id', 'name', 'image']


#use on get request
class UserSerializer(serializers.ModelSerializer):
    image_Id = ImageSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'role', 'image_Id', 'email', 'street_Address', 'city', 'state', 'zip_Code', 'phone']


#Use to Post,Put or Delete
class PostClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothing
        fields = ['id', 'image_Id', 'user_Id', 'type', 'brand', 'style', 'material', 'pattern', 'size', 'color']


#use on post, put or delete
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'user_Id', 'item_Id', 'name', 'image']


#use on get request
class ClothingSerializer(serializers.ModelSerializer):
    image_Id = ImageSerializer(read_only=True)#includes image on get

    class Meta:
        model = Clothing
        fields = ['id', 'image_Id', 'user_Id', 'type', 'brand', 'style', 'material', 'pattern', 'size', 'color']


#use on get request
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user_Id', 'name', 'number_Items', 'price', 'delivery_Freq']


#Use to Post,Put or Delete
class PostSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user_Id', 'name', 'number_Items', 'price', 'delivery_Freq']


#use on get request
class OrderSerializer(serializers.ModelSerializer):
    user_Id = UserSerializer(read_only=True) #includes user on get
    subscription_Id = SubscriptionSerializer(read_only=True)#includes subscription on get
    clothing_Items = ClothingSerializer(read_only=True, many=True)#includes all clothing in get

    class Meta:
        model = Order
        fields = ['id', 'user_Id', 'subscription_Id', 'clothing_Items', 'total', 'est_Delivery']


#Use to Post,Put or Delete
class PostOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user_Id', 'subscription_Id', 'clothing_Items', 'total', 'est_Delivery']


