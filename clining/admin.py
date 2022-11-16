from django.contrib import admin
from .models import *


admin.site.register(SubServices)
admin.site.register(CardServices)
# admin.site.register(Order)
admin.site.register(Service)
admin.site.register(Room)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [
        'roomname','roomprice','servicename'
    ]
    class Meta:
        model = Orders

admin.site.register(Orders, OrdersAdmin)
