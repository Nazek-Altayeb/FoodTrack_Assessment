from rest_framework import  status
from django.http import JsonResponse
from rest_framework import serializers
from .models import Store
from .serializers import  StoreSerializer, FoodsSerializer, OpeningHoursSerializer, OpeningHoursSerializerDetail
from rest_framework.decorators import api_view, api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import *



@api_view(['GET', 'POST'])
def stores(request):
    if request.method == 'GET':
        stores= Store.objects.all()
        storeSerializer = StoreSerializer(stores, many=True)
        return JsonResponse({'stores':storeSerializer.data}, safe=False)
        """return Response(storeSerializer.data, status=200)"""
    if request.method == 'POST':
        storeSerializer = StoreSerializer(data = request.data)
        if storeSerializer.is_valid():
            storeSerializer.save()
            return Response(storeSerializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(storeSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def openingHours(request):
    if request.method == 'GET':
        openingHours= OpeningHours.objects.all()
        openingHoursSerializer = OpeningHoursSerializerDetail(openingHours, many=True)
        return JsonResponse({'openingHours':openingHoursSerializer.data}, safe=False)
        """return Response(storeSerializer.data, status=200)"""
    if request.method == 'POST':
        openingHoursSerializer = OpeningHoursSerializerDetail(data = request.data)
        if openingHoursSerializer.is_valid():
            openingHoursSerializer.save()
            return Response(openingHoursSerializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(openingHoursSerializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def foods(request):
    if request.method == 'GET':
        foods= Foods.objects.all()
        foodsSerializer = FoodsSerializer(foods, many=True)
        return JsonResponse({'foods':foodsSerializer.data}, safe=False)
        """return Response(storeSerializer.data, status=200)"""
    if request.method == 'POST':
        foodsSerializer = FoodsSerializer(data = request.data)
        if foodsSerializer.is_valid():
            foodsSerializer.save()
            return Response(foodsSerializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(foodsSerializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])       
def store_detail(request, pk):
    try:
        store = Store.objects.get(id = pk)
    except Store.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        storeSerializer = StoreSerializer(store)
        return Response(storeSerializer.data)

    elif request.method == 'PUT':
        storeSerializer = StoreSerializer(store, data = request.data)
        if storeSerializer.is_valid():
            storeSerializer.save()
            return Response(storeSerializer.data)
        return Response(storeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        store.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'PUT', 'DELETE']) 
def food_detail(request, pk):
    try:
        food_item = Foods.objects.get(id = pk)
    except Foods.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        foodSerializer = FoodsSerializer(food_item)
        return Response(foodSerializer.data)

    elif request.method == 'PUT':
        foodSerializer = FoodsSerializer(food_item, data = request.data)
        if foodSerializer.is_valid():
            foodSerializer.save()
            return Response(foodSerializer.data)
        return Response(foodSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food_item.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'PUT', 'DELETE']) 
def openingHour_detail(request, pk):
    try:
        openingHour = OpeningHours.objects.get(id = pk)
    except OpeningHours.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        openingHoursSerializer = OpeningHoursSerializerDetail(openingHour)
        return Response(openingHoursSerializer.data)

    elif request.method == 'PUT':
        openingHoursSerializer = OpeningHoursSerializerDetail(openingHour, data = request.data)
        if openingHoursSerializer.is_valid():
            openingHoursSerializer.save()
            return Response(openingHoursSerializer.data)
        return Response(openingHoursSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        openingHour.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)


"""@api_view(["GET", "POST"])
def openingHours(self, request, id=None):
    if request.method == 'GET':
        store = self.get_object()
        openingHours = OpeningHours.objects.filter(store=store)
        serializer = OpeningHoursSerializer(openingHours, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        store = self.get_object()
        data = request.data
        data["store"] = store.id
        serializer = OpeningHoursSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)"""

    


"""@api_view(["GET"])
def food(self, request, id=None):
    if request.method == 'GET':
        store = self.get_object()
        food = Food.objects.filter(store=store)
        serializer = FoodSerializer(openingHours, many=True)
        return Response(serializer.data, status=200)
    if request.method == 'POST':
        store = self.get_object()
        data = request.data
        data["store"] = store.id
        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)"""
    

