from rest_framework import serializers
from .models import Store, Address, OpeningHours


class AddressSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    city = serializers.CharField()
    state = serializers.CharField()
    zipcode = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ['id', 'city', 'state', 'zipcode']


class StoreSerializer(serializers.ModelSerializer):

    """
    Serializer for the Store model
    """
    name = serializers.CharField()
    openingHours = serializers.CharField()
    address = AddressSerializer()

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'openingHours']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)
        new_store = Store.objects.create(**validated_data, address=address)
        return new_store
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        address_id = address_data.get('id')
        instance.name = validated_data.get('name', instance.name)
        instance.openingHours = validated_data.get('openingHours', instance.openingHours)
        instance.save()
        
        existing_address = Address.objects.get(pk=address_id)
        
        existing_address.city = address_data.get('city', existing_address.city)
        existing_address.state = address_data.get('state', existing_address.state)
        existing_address.zipcode = address_data.get('zipcode', existing_address.zipcode)
        existing_address.save()

        return instance




