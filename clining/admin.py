from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin




class OrderCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    class Meta:
        model = OrderCategory
admin.site.register(OrderCategory, OrderCategoryAdmin)


class OrderFormAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'email', 'phone_number', 'category'
    ]
    list_display_links = ['name', 'email']
    class Meta:
        model = OrderForm
admin.site.register(OrderForm, OrderFormAdmin)


@admin.register(CaruselImage)
class CaruselImageAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['id', 'name']


@admin.register(CaruselDetail)
class CaruselDetailAdmin(TranslationAdmin):
    list_display = ['id', 'carusel', 'title', 'description']
    list_display_links = ['id', 'title']




@admin.register(Project)
class ProjectDetailAdmin(TranslationAdmin):
    list_display = ['id', 'gallary', 'title', 'description']
    list_display_links = ['id', 'title', 'description']


@admin.register(Room2)
class ProjectDetailAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id', 'name', 'description']





class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    list_display_links = ['id', 'key']
    class Meta:
        model = Settings
admin.site.register(Settings, SettingsAdmin)


@admin.register(GallaryCategory)
class GallaryCategoryAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'image']
    list_display_links = ['id', 'name']


@admin.register(GallaryDetail)
class GallaryDetailAdmin(TranslationAdmin):
    list_display = ['id', 'gallary', 'title', 'description']
    list_display_links = ['id', 'gallary', 'title']



@admin.register(CardServices)
class CardServicesAdmin(TranslationAdmin):
    list_display = ['id', 'services', 'name', 'price', 'detail']
    list_display_links = ['id', 'name', 'price']

    def services(self, obj):
        return len(obj.service.all())
    services.short_description = 'service'

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).prefetch_related('service')



@admin.register(SubServices)
class SubServicesAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'is_exist']
    list_display_links = ['id', 'name']



class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'description']
    list_display_links = ['id', 'name','description']
    class Mate:
        model = ContactForm
admin.site.register(ContactForm, ContactFormAdmin)


@admin.register(Room)
class RoomCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'price'
    ]
    list_display_links = ['name']


@admin.register(Service)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['name']




# class OrdersAdmin(admin.ModelAdmin):
#     list_display = [
#         'roomname', 'roomprice', 'servicename'
#     ]
#     class Meta:
#         model = Orders

# admin.site.register(Orders, OrdersAdmin)