from django.urls import path
from .views import *

app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('gallary_details/', gallary_details, name='gallary_details'),
    path('gallary/', gallary, name='gallary'),
    path('guests/', guests, name='guests'),
    path('services/', services, name='services'),

    path('roomcategory/', RoomCategoryAPIView.as_view()),
    path('serviceprice/', ServicePriceAPIView.as_view())
]
