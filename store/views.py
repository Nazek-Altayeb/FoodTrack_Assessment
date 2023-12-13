from django.http import JsonResponse
from .models import Store, Address, OpeningHours
from .serializers import StoreSerializer

def stores(request):
    stores= Store.objects.all()
    storeSerializer = StoreSerializer(stores, many=True)
    return JsonResponse({'stores':storeSerializer.data}, safe=False)