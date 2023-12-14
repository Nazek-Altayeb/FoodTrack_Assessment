from django.http import JsonResponse
from rest_framework import serializers
from .models import Store, Address, OpeningHours
from .serializers import StoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def stores(request):
    if request.method == 'GET':
        stores= Store.objects.all()
        storeSerializer = StoreSerializer(stores, many=True)
        return JsonResponse({'stores':storeSerializer.data}, safe=False)
    if request.method == 'POST':
        storeSerializer = StoreSerializer(stores = request.data)
        if storeSerializer.is_valid():
            storeSerializer.save()
            return Response(storeSerializer.data, status= status.HTTP_201_CREATED)



