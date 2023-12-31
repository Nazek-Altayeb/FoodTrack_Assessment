from rest_framework import  status
from django.http import JsonResponse
from .models import Store
from .serializers import  StoreSerializer, OpeningHoursSerializerDetail, FoodsSerializerDetail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *



@api_view(['GET', 'POST'])
def stores(request):
    if request.method == 'GET':
        stores= Store.objects.all()
        storeSerializer = StoreSerializer(stores, many=True)
        return JsonResponse({'stores':storeSerializer.data}, safe=False)
    if request.method == 'POST':
        storeSerializer = StoreSerializer(data = request.data)
        if storeSerializer.is_valid():
            storeSerializer.save()
            return Response(storeSerializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(storeSerializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

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
    

@api_view(['GET'])
def openingHours(request):
        openingHours= OpeningHours.objects.all()
        openingHoursSerializer = OpeningHoursSerializerDetail(openingHours, many=True)
        return JsonResponse({'openingHours':openingHoursSerializer.data}, safe=False)
        

@api_view(['POST'])
def add_openingHour(request, pk):
        store_object = Store.objects.get(id = pk)
        data = request.data
        print('DATA:', data)

        """ review, created = Foods.objects.get_or_create(
            store = store_object,  
        )"""
        created = OpeningHours.objects.create(
            store = store_object,
            branch = data['branch'],
            day = data['day'],
            open_at = data['open_at']
        )

        print('store' , store_object)

        created.branch = data['branch']
        created.day = data['day']
        created.open_at = data['open_at']
        created.save()

        storeSerializer = StoreSerializer(store_object, many = False)
        return Response(storeSerializer.data, status= status.HTTP_201_CREATED) 


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


@api_view(['GET'])
def foods(request):
    if request.method == 'GET':
        foods= Foods.objects.all()
        foodsSerializer = FoodsSerializerDetail(foods, many=True)
        return JsonResponse({'foods':foodsSerializer.data}, safe=False)


@api_view(['POST'])
def add_food(request,pk):
        store_object = Store.objects.get(id = pk)
        data = request.data
        print('DATA:', data)

        """ review, created = Foods.objects.get_or_create(
            store = store_object,  
        )"""
        created = Foods.objects.create(
            store = store_object,
            foodName = data['foodName'],
            salesPerDay = data['salesPerDay'],
            returnedItemsPerDay = data['returnedItemsPerDay']
        )

        print('store' , store_object)

        created.foodName = data['foodName']
        created.salesPerDay = data['salesPerDay']
        created.returnedItemsPerDay = data['returnedItemsPerDay']
        created.save()

        storeSerializer = StoreSerializer(store_object, many = False)
        return Response(storeSerializer.data, status= status.HTTP_201_CREATED)

    
@api_view(['GET', 'PUT', 'DELETE']) 
def food_detail(request, pk):
    try:
        food_item = Foods.objects.get(id = pk)
    except Foods.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        foodSerializer = FoodsSerializerDetail(food_item)
        return Response(foodSerializer.data)

    elif request.method == 'PUT':
        foodSerializer = FoodsSerializerDetail(food_item, data = request.data)
        if foodSerializer.is_valid():
            foodSerializer.save()
            return Response(foodSerializer.data)
        return Response(foodSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        food_item.delete()
        return Response(status =status.HTTP_204_NO_CONTENT)
    

"""class CustomResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000"""


    

