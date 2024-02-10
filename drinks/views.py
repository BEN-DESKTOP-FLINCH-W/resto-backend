from django.http import JsonResponse
from .models import Drinks
from .models import Users
from .models import Restaurants
from .serializers import DrinksSerializer
from .serializers import UsersSerializer
from .serializers import UserSerializer
from .serializers import RestaurantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def drink_list(request, format=None):
    if request.method =='GET':
        drinks=Drinks.objects.all()
        serializer= DrinksSerializer(drinks, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=DrinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id, format=None):

    try:
        drink=Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer= DrinksSerializer(drink)
        return Response(serializer.data)
       
    elif request.method=='PUT':
        serializer=DrinksSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def add_user(request,format=None):
    if request.method=='POST':
        serializer=UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def auth_user(request,email,password, format=None):
    try:
        user=Users.objects.get(email=email, password=password)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT) 
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET','POST'])
def restaurant_list(request, format=None):
    if request.method =='GET':
        restaurants=Restaurants.objects.all()
        serializer= RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer=RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def restaurant_detail(request,id, format=None):

    try:
        restaurant=Restaurants.objects.get(pk=id)
    except Restaurants.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer= RestaurantSerializer(restaurant)
        return Response(serializer.data)
       
    elif request.method=='PUT':
        serializer=RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_200_OK)