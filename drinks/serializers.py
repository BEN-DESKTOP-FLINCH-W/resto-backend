from rest_framework import serializers
from .models import Drinks
from .models import Users
from .models import Restaurants

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drinks
        fields=['id','name','description']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['id','name','email','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=['email','password']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Restaurants
        fields=['id','name','contact','address']


