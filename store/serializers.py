from rest_framework import serializers
from .models import Store, Address, OpeningHours



class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'city', 'state', 'zipcode']



class StoreSerializer(serializers.ModelSerializer):

    """
    Serializer for the Store model
    """
    address = AddressSerializer(many=False)

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'openingHours']

   
