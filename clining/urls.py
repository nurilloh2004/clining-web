from django.urls import path
from .views import *

app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallary_details/', gallary_details, name='gallary_details'),
    path('product-detail/<int:pk>/', product_detail, name='product_detail'),
    path('gallary/', gallary, name='gallary'),
    path('guests/', guests, name='guests'),
    path('services/', services, name='services'),
    path('product_detail/', product_detail, name='product_detail'),
    path('roomcategory/', RoomCategoryAPIView.as_view()),
    path('serviceprice/', ServicePriceAPIView.as_view())
]
