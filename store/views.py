from django.http import JsonResponse
from rest_framework import serializers
from .models import Store, Address
from .serializers import StoreSerializer, AddressSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics



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
        pass



