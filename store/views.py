from django.http import JsonResponse
from rest_framework import serializers
from .models import Store, Address, OpeningHours
from .serializers import StoreSerializer

def stores(request):
    stores= Store.objects.all()
    storeSerializer = StoreSerializer(stores, many=True)
    return JsonResponse({'stores':storeSerializer.data}, safe=False)



    """def get_opening_hours(self, obj):
        name = obj.name
        openingHours = name.openingHours.all()
        print(f'openingHours: {openingHours}')
        return FollowerNameSerializer(openingHours, many=True).data"""