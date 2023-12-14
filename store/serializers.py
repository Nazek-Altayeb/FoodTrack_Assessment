from rest_framework import serializers
from .models import Store, Address, OpeningHours


class AddressSerializer(serializers.ModelSerializer):

    """  city = serializers.ReadOnlyField()
    state = serializers.ReadOnlyField()
    zipcode = serializers.ReadOnlyField()"""

    """store = StoreSerializer(read_only=True, many=False)"""
    class Meta:
        model = Address
        fields = ['id', 'city', 'state', 'zipcode']


class StoreSerializer(serializers.ModelSerializer):

    """
    Serializer for the Store model
    """
    name = serializers.ReadOnlyField()
    openingHours = serializers.ReadOnlyField()
    """address = AddressSerializer(read_only=True, many=False)"""
    address = AddressSerializer()

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'openingHours']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        new_store = Store.objects.create(**validated_data, address=address)
        return new_store




