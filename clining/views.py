import keyword
import string

from django.shortcuts import render, redirect
from .models import *
# from .serializers import ServicePriceSerializers, RoomCategorySerializers, OrdersSerialiser
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *
from rest_framework import generics



# class RoomCategoryAPIView(generics.CreateAPIView):
#     # queryset = OrderItem.objects.all()
#     # serializer_class = OrdersSerialiser


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



# class ServicePriceAPIView(APIView):
#     def get(self, request):
#         return Response({
#             'servicecategoryprice': ServicePriceSerializers(Service.objects.all(), many=True).data
#         })
    
#     def post(self, request):
#         data = OrdersSerialiser(data=request.data)
#         if data.is_valid():
#             return Response({
#                 'status': "Post qo'shildi",
#                 'data': data.errors
#             })
#         data.save()
#         return Response({
#             'status': 'success',
#             'data': OrdersSerialiser(data.instance).data
#         })


def home(request):
    caruselimg = CaruselImage.objects.filter()
    form = OrderModelForm()
    if request.method == 'POST':
        form = OrderModelForm(request.POST)
        # print("QWERTYTREAWERT------------", form)
        if form.is_valid():
            print('AAAAAAAAA------', form)
            form.save()
            return redirect('myprint:home')
        else:
            print("TTTTTTTTTTTT------------>>>>>>>", form.errors)
            form = OrderModelForm()
            print("SSSSSSSSSSSSSS------------>>>>>>>", form.errors)
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
            return redirect('myprint:home')
        else:
            form = ContactModelForm()
    context = {
        'form': form
    }
    return render(request, 'main/contact.html', context=context)


def gallary(request):
    det = Room2.objects.all()
    context = {
        'det': det,
    }
    return render(request, 'main/gallary.html', context=context)


def gallary_details(request, pk):
    project = Project.objects.filter(gallary_id=pk)
    context = {
        'project': project,
    }
    return render(request, 'main/gallary-datails.html', context=context)




def guests(request):
    card = CardServices.objects.all()
    cat = RoomGuest.objects.all()
    servic = ServiceGuest.objects.all()
    if request.method == "POST":
        name = request.POST.get('let[]')
        print('>>>>>>>>>>>>>>>>>>>', name)
        phone_number = request.POST.get('lett[]')
        print('>>>>>>>>>>>>>>>>>>>', phone_number)
        services = request.POST.getlist('checks[]')
        print('>>>>>>>>>>>>>>>>>>>', services)
        house = request.POST.get('option[]').split("-")
        print('>>>>>>>>>>>>>>>>>>>', house)
        house_name = house[0]
        house_price = int(house[1])
        house = OrdersGuest.objects.create(roomname=house_name, roomprice=house_price, servicename=services, user_name=name, user_phone_number=phone_number)
        house.save()
            
        return redirect('myprint:contact')
    context = {
        'cat': cat, 
        'servic': servic,
        'card': card,
    }
    return render(request, 'main/guests.html', context)




























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
#         service = Service.objects.create(ser)
#         # service_name = services[0]
#         # service_price = int(services[1])
#         order = Order.objects.create(roomname=house_name, roomprice=house_price)
#         order.service.add()
#         order.save()
#         return redirect('myprint:services')
#     context = {
#         'cat': cat,
#         'card': card,
#         'pr': pr
#     }
#     return render(request, 'main/services.html', context=context)




def info_order(request):
    info = Orders.objects.all()
    total = 0


    context={'info': info}
    return render(request, 'service-info.html', context)



# def services(request):
#     card = CardServices.objects.all()
#     cat = Room.objects.all()
#     servic = Service.objects.all()
#     if request.method == "POST":
#         services = request.POST.getlist('checks[]')
#         house = request.POST.get('option[]').split("-")
#         total = 0
#         house_name = house[0]
#         house_price = int(house[1])
#         service_name = services[0]
#         service_price = int(services[1])
#         tt = house_price + service_price
#         tts = Total.objects.create(total = tt)
#         tts.save()
 
#         order = Orders.objects.create(roomname=house_name, roomprice=house_price, servicename=service_name, serviceprice=service_price, total_price=total)
#         order.save()
#         return redirect('myprint:home')
#     context = {
#         'cat': cat,
#         'card': card,
#         'servic': servic
#     }
#     return render(request, 'main/services.html', context=context)




def services(request):
    card = CardServices.objects.all()
    cat = Room.objects.all()
    servic = Service.objects.all()
    if request.method == "POST":
        name = request.POST.get('let[]')
        print('>>>>>>>>>>>>>>>>>>>', name)
        phone_number = request.POST.get('lett[]')
        print('>>>>>>>>>>>>>>>>>>>', phone_number)
        services = request.POST.getlist('checks[]')
        print('>>>>>>>>>>>>>>>>>>>', services)
        house = request.POST.get('option[]').split("-")
        print('>>>>>>>>>>>>>>>>>>>', house)
        house_name = house[0]
        house_price = int(house[1])
        house = Orders.objects.create(roomname=house_name, roomprice=house_price, servicename=services, user_name=name, user_phone_number=phone_number)
        house.save()
            
        return redirect('myprint:contact')
    context = {
        'cat': cat, 
        'servic': servic,
        'card': card,
    }
    return render(request, 'main/services.html', context=context)
