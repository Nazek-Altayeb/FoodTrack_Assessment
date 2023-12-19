from rest_framework import serializers
from .models import Store, Address, OpeningHours, Foods


class AddressSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    city = serializers.CharField()
    street = serializers.CharField()
    zipcode = serializers.IntegerField()

    class Meta:
        model = Address
        fields = ['id', 'city', 'street', 'zipcode']


class OpeningHoursSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    day = serializers.CharField()
    open_at = serializers.TimeField()
    branch = serializers.CharField()
    
    class Meta:
        model = OpeningHours
        fields = ['id' ,'day', 'open_at', 'branch']
    

class OpeningHoursSerializerDetail(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    day = serializers.CharField()
    open_at = serializers.TimeField()
    store = serializers.ReadOnlyField(source='store.name')
    branch = serializers.ReadOnlyField()
    """store_branch = serializers.SerializerMethodField()"""
    
    class Meta:
        model = OpeningHours
        fields = ['id', 'store', 'branch', 'day', 'open_at']

    def get_store_branch(self, obj):
        return '{} {}'.format(obj.store, obj.branch)


class FoodsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    foodName = serializers.CharField()
    salesPerDay = serializers.IntegerField()
    returnedItemsPerDay = serializers.IntegerField()
    store = serializers.ReadOnlyField(source='store.name')

    class Meta:
        model = Foods
        fields = ['id', 'store', 'foodName', 'salesPerDay', 'returnedItemsPerDay']
       



class StoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
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
        foods = validated_data.pop('foods')
       
        address = Address.objects.create(**address_data)
        new_store = Store.objects.create(**validated_data, address=address)
       
        for openingHour in openingHours_data:
            OpeningHours.objects.create(**openingHour, store = new_store)
        for food_item in foods:
            Foods.objects.create(**food_item, store = new_store)    

        return new_store
    

    def update(self, instance, validated_data):
        foods = validated_data.pop('foods')
        address_data = validated_data.pop('address')
        openingHours = validated_data.pop('openingHours')
        address_id = address_data.get('id')
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        """
        Update the address details for specific store
        """
        existing_address = Address.objects.get(pk=address_id)
        existing_address.city = address_data.get('city', existing_address.city)
        existing_address.street = address_data.get('street', existing_address.street)
        existing_address.zipcode = address_data.get('zipcode', existing_address.zipcode)
        existing_address.save()

        """
        Update the foods objects for specific store
        """
        kept_foods = []
        for food in foods:
            if "id" in food.keys():
                if Foods.objects.filter(id=food["id"]).exists():
                    c = Foods.objects.get(id=food["id"])
                    c.foodName = food.get('foodName', c.foodName)
                    c.salesPerDay = food.get('salesPerDay', c.salesPerDay)
                    c.returnedItemsPerDay = food.get('returnedItemsPerDay', c.returnedItemsPerDay)
                    c.save()
                    kept_foods.append(c.id)
                else:
                    continue
            else:
                c = Foods.objects.create(**food, store=instance)
                kept_foods.append(c.id)

        """for food in instance.foods:
            if food.id not in kept_foods:
                food.delete()"""

        """
        Update the opening hours objects for specific store
        """
        kept_openingHours = []
        for openingHour in openingHours:
            if "id" in openingHour.keys():
                if OpeningHours.objects.filter(id=openingHour["id"]).exists():
                    c = OpeningHours.objects.get(id=openingHour["id"])
                    c.day = openingHour.get('day', c.day)
                    c.open_at = openingHour.get('open_at', c.open_at)
                    c.save()
                    kept_openingHours.append(c.id)
                else:
                    continue
            else:
                c = OpeningHours.objects.create(**openingHour, store=instance)
                kept_openingHours.append(c.id)

        """for openingHour in instance.openingHours:
            if openingHour.id not in kept_openingHours:
                openingHour.delete()"""


        return instance