import keyword
import string

from django.shortcuts import render, redirect
from .models import *
from .serializers import ServicePriceSerializers, RoomCategorySerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *


class RoomCategoryAPIView(APIView):
    def get(self, request):
        return Response({
            'categoryroom': RoomCategorySerializers(RoomCategory.objects.all(), many=True).data
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



class ServicePriceAPIView(APIView):
    def get(self, request):
        return Response({
            'servicecategoryprice': ServicePriceSerializers(ServiceType.objects.all(), many=True).data
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

def services(request):
    card = CardServices.objects.all()
        
    context = {'card': card,}
    return render(request, 'main/services.html', context)




def product_detail(request, pk):
    detailCarusel = CaruselDetail.objects.filter(carusel_id=pk)
    context = {
        'detailCarusel': detailCarusel
    }
    return render(request, 'main/product-details.html', context=context)



