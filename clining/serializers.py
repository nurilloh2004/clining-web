from rest_framework import serializers
from .models import *




class ServicePriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id', 'name', 'price')


class RoomCategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = RoomCategory
        fields = ('id', 'name', 'price')



class OrdersSerialiser(serializers.ModelSerializer):

    class Mera:
        model = Orders
        fields = ('id', 'roomname', 'roomprice', 'servicename', 'serviceprice', 'total')



