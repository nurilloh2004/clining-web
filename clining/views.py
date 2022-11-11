import keyword
import string

from django.shortcuts import render, redirect
from .models import *
from .serializers import ServicePriceSerializers, RoomCategorySerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class RoomCategoryAPIView(APIView):
    def get(self, request):
        return Response({
            'categoryroom': RoomCategorySerializers(RoomCategory.objects.all(), many=True).data
        })

    def post(self, request):
        data = RoomCategorySerializers(data=request.data)
        if data.is_valid():
            return Response({
                'status': "Post qo'shildi",
                'data': data.errors
            })
        data.save()
        return Response({
            'status': 'success',
            'data': RoomCategorySerializers(data.instance).data
        })


class ServicePriceAPIView(APIView):
    def get(self, request):
        return Response({
            'servicecategoryprice': ServicePriceSerializers(Price.objects.all(), many=True).data
        })

    def post(self, request):
        data = ServicePriceSerializers(data=request.data)
        if data.is_valid():
            return Response({
                'status': "Post qo'shildi",
                'data': data.errors
            })
        data.save()
        return Response({
            'status': 'success',
            'data': ServicePriceSerializers(data.instance).data
        })




def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def gallary_details(request):
    return render(request, 'main/gallary-details.html')

def gallary(request):
    return render(request, 'main/gallary.html')


def guests(request):
    return render(request, 'main/guests.html')

def services(request):
    return render(request, 'main/services.html')

# def services(request):
#     cat = RoomCategory.objects.all()
#     pr = Price.objects.all()
#     if request.method == "POST":
#         check = request.POST.getlist('checks[]')
#         option = request.POST.getlist('option[]')
#         print("WWWWWWWWWWW_______>>>>>>>>>", check)
#         print("OOOOOOOOOOO_______>>>>>>>>>", option)
#         # req_obj = Orders.objects.create(nameroom=option, nameservice=check)
#         # req_obj.save()
#         return redirect('myprint:services')
#     context = {
#         'cat': cat,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)


# def services(request):
#     cat = RoomCategory.objects.all()
#     pr = Price.objects.all()
#     if request.method == "POST":
#         services = request.POST.getlist()
#         house = request.POST.get('option[]').split("-")
#         print("aaaaaaaaaaaa-------------", house)
#         house_name = house[0]
#         house_price = int(house[1])
#         for service in services:
#             service = service.split("-")
#             service_name = service[0]
#             service_price = service[1]
#             new_order = Orders.objects.create(roomname=house_name, roomprice=house_price, servicename=service_name, serviceprice=service_price)
#             new_order.save()
#         return redirect('myprint:services')
#     context = {
#         'cat': cat,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)