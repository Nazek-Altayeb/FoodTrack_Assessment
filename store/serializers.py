from rest_framework import serializers
from .models import Store, Address, OpeningHours


class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Store model
    """

    class Meta:
        model = Store
        fields = ['id', 'name', 'address', 'openingHours']