from rest_framework import serializers
from .models import *

from django.core import serializers
from rest_framework import serializers


class ServicePriceSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(source='name')
    # name = serializers.PositiveIntegerField(source='price')
    class Meta:
        model = Service
        fields = ('id', 'name', 'price')

class RoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ('id', 'name', 'price')



class OrdersSerialiser(serializers.ModelSerializer):
    # name = ServicePriceSerializers(many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'room', 'service']
        read_only_fields = ['id']

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data["service"] = ServicePriceSerializers(instance.service).data
            return data


