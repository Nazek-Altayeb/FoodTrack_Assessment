from rest_framework import serializers
from .models import Store, Address, OpeningHours, Foods


class AddressSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    city = serializers.CharField()
    state = serializers.CharField()
    zipcode = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ['id', 'city', 'state', 'zipcode']


class OpeningHoursSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    day = serializers.CharField()
    time = serializers.TimeField()

    class Meta:
        model = OpeningHours
        fields = ['id', 'day', 'time']


class FoodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    foodName = serializers.CharField()
    salesPerDay = serializers.IntegerField()
    returnedItemsPerDay = serializers.IntegerField()

    class Meta:
        model = Foods
        fields = ['id', 'foodName', 'salesPerDay', 'returnedItemsPerDay'] 



class StoreSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    address = AddressSerializer()
    openingHours = OpeningHoursSerializer(many= True)
    foods = FoodsSerializer(many= True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'openingHours', 'foods']


    def create(self, validated_data):
        address_data = validated_data.pop('address')
        openingHours_data = validated_data.pop('openingHours')
        food_data = validated_data.pop('food')
        address = Address.objects.create(**address_data)
        new_store = Store.objects.create(**validated_data, address=address)
        for openingHour in openingHours_data:
            OpeningHours.objects.create(**openingHour, store = new_store)
        for food_item in food_data:
            Foods.objects.create(**food_item, store = new_store)    

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