import keyword
import string

from django.shortcuts import render, redirect
from .models import *
from .serializers import ServicePriceSerializers, RoomCategorySerializers, OrdersSerialiser
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from rest_framework import generics



class RoomCategoryAPIView(generics.CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrdersSerialiser


# class RoomCategoryAPIView(APIView):
#     def get(self, request):
#         return Response({
#             'categoryroom': RoomCategorySerializers(RoomCategory.objects.all(), many=True).data
#         })

        
    
#     def post(self, request):
#         services: list = request.POST.getlist('services')
#         for item in services:
#             # {name: "ser-1", price: 35},
#             # {name: "ser-2", price: 25}
#             pass
#         data = OrdersSerialiser(data=request.data)
#         if data.is_valid():2
#             return Response({
#                 'status': "Post qo'shildi",
#                 'data': data.errors
#             })
#         data.save()
#         return Response({
#             'status': 'success',
#             'data': OrdersSerialiser(data.instance).data
#         })



class ServicePriceAPIView(APIView):
    def get(self, request):
        return Response({
            'servicecategoryprice': ServicePriceSerializers(Service.objects.all(), many=True).data
        })
    
    def post(self, request):
        data = OrdersSerialiser(data=request.data)
        if data.is_valid():
            return Response({
                'status': "Post qo'shildi",
                'data': data.errors
            })
        data.save()
        return Response({
            'status': 'success',
            'data': OrdersSerialiser(data.instance).data
        })


def home(request):
    caruselimg = CaruselImage.objects.filter()
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprint:home')
        else:
            form = OrderModelForm()
    context = {
        'form': form,
        'caruselimg': caruselimg,

    }
    return render(request, 'main/index.html', context=context)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    form = ContactModelForm()
    if request.method == "POST":
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprint:contact')
        else:
            form = ContactModelForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context=context)


def gallary_details(request):
    return render(request, 'main/gallary-details.html')

def gallary(request):
    return render(request, 'main/gallary.html')


def guests(request):
    return render(request, 'main/guests.html')




























def product_detail(request, pk):
    detailCarusel = CaruselDetail.objects.filter(carusel_id=pk)
    context = {
        'detailCarusel': detailCarusel
    }
    return render(request, 'main/product-details.html', context=context)


















# def services(request):
#     card = CardServices.objects.all()
#     cat = Room.objects.all()
#     pr = Service.objects.all()
#     if request.method == "POST":
#         services = request.POST.getlist('checks[]')
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
#         'card': card,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)



# def services(request):
#     card = CardServices.objects.all()
#     cat = Room.objects.all()
#     pr = Service.objects.all()
#     if request.method == "POST":
#         services = request.POST.getlist('checks[]')
#         house = request.POST.get('option[]').split("-")
#         print(">>>>>>>>>>>>>>>>>>>>>>>>", house)
#         print("aaaaaaaaaaaa-------------", services)
#         house_name = house[0]
#         house_price = int(house[1])
#         total = 0
#         for ser in services:
#             print(">>>>>>>>>>>>>>>>>>>>>", ser)
#             ser = ser.split("-")
#             service_name = ser[0]
#             service_price = int(ser[1])
#             total += service_price
#             order = Order.objects.create(roomname=house_name, roomprice=house_price, total=total)
#             order.save()
#             order.service.add(ser)
#         return redirect('myprint:services')
#     context = {
#         'cat': cat,
#         'card': card,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)



def services(request):
    card = CardServices.objects.all()
    cat = Room.objects.all()
    pr = Service.objects.all()
    if request.method == "POST":
        services = request.POST.getlist('checks[]')
        house = request.POST.get('option[]').split("-")
        print(">>>>>>>>>>>>>>>>>>>>>>>>", house)
        print("aaaaaaaaaaaa-------------", services)
        house_name = house[0]
        house_price = int(house[1])
        service = Service.objects.create(ser)
        # service_name = services[0]
        # service_price = int(services[1])
        order = Order.objects.create(roomname=house_name, roomprice=house_price)
        order.service.add()
        order.save()
        return redirect('myprint:services')
    context = {
        'cat': cat,
        'card': card,
        'pr': pr
    }
    return render(request, 'main/services.html', context=context)




def info_order(request):
    info = Orders.objects.all()
    total = 0


    context={'info': info}
    return render(request, 'service-info.html', context)