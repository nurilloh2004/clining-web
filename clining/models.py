from django.db import models
from django.utils.translation import gettext_lazy as _


# Hope Page

class OrderCategory(models.Model):
    name = models.CharField(_('name'),max_length=65)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub Order Category"

class OrderForm(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'), max_length=60)
    phone_number = models.IntegerField(_('phone_number'), )
    category = models.ForeignKey(OrderCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Order Form"




# Home Image Carusel Category
class CaruselImage(models.Model):
    name = models.CharField(_('name'), max_length=50)
    image = models.ImageField(_('image'), upload_to='media/carusel')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Karusel"


#  Home Carusel Detaile
class CaruselDetail(models.Model):
    carusel = models.ForeignKey(CaruselImage, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Carusel Detail"

#  Doimiy Sozlamalar
class Settings(models.Model):
    key = models.CharField(_('key'), max_length=50)
    value = models.CharField(_('value'), max_length=500)
    def __str__(self):
        return self.key
    class Meta:
        verbose_name = "Sozlamalar"

# Gallereya uchun Kategoriya
class GallaryCategory(models.Model):
    name = models.CharField(_('name'), max_length=50)
    image = models.ImageField(_('image'), upload_to="media/gallary")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Gallary Category"

# Gallereya Tavsiloti
class GallaryDetail(models.Model):
    gallary = models.ForeignKey(GallaryCategory, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=200)
    description = models.TextField(_('description'))
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Gallery Detail'

#  Xizmatlar



class SubServices(models.Model):
    name = models.CharField(_('name'), max_length=50)
    # detail = models.CharField(_('detail'), max_length=65)
    is_exist = models.BooleanField(_('is_exist'), default=True)
    def __str__(self):
        return f"{self.name} | {self.is_exist}"

    class Meta:
        verbose_name = "Sub Card Xizmatlar"


class CardServices(models.Model):
    service = models.ManyToManyField(SubServices)
    name = models.CharField(_('name'), max_length=100)
    price = models.PositiveIntegerField(_('price'), )
    detail = models.TextField(_('detail'), )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Card Xizmatlar'




#forms
class ContactForm(models.Model):
    name = models.CharField(_('name'), max_length=50)
    email = models.EmailField(_('email'), max_length=60)
    phone_number = models.IntegerField(_('phone_number'))
    description = models.TextField(_('description'), max_length=550)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kontakt"

# class ServiceType(models.Model):
#     name = models.CharField(_('name'), max_length=120, blank=True, null=True)
#     price = models.PositiveIntegerField(_('price'),)
#     def __str__(self):
#         return f"{self.name} {str(self.price)}"
#     class Meta:
#         verbose_name = "Xizmat kursatish turlari"



# class RoomCategory(models.Model):
#     name = models.CharField(_('name'), max_length=100, blank=True, null=True)
#     price = models.PositiveIntegerField(_('price'), )
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name = "Xona turlari"


# class Orders(models.Model):
#     roomname = models.CharField(_('roomname'), max_length=100)
#     roomprice = models.PositiveIntegerField(_('roomprice'), )
#     servicename = models.CharField(_('servicename'), max_length=100)
#     serviceprice = models.PositiveIntegerField(_('serviceprice'), )
#     total = models.PositiveIntegerField(_('total'), )  # 150
    
#     def __str__(self):
#         return f"{str(self.roomname)} {str(self.roomprice)}"

# qani bunda choice hullas sal modellarni xato tuzib qoyibsizda shu serviceni ham orderni ichiga qsez yaxwi bo`lardi`
#masalan qande bo'ladi 
#bu code lar github da bor be malol o'zgartirsa bo'laveradi shuni tuzib berolasizmi hoz
#hozrmasu bugun qilib berolishim mumkun
class Service(models.Model):
    name = models.CharField(_('name'), max_length=120, blank=True, null=True)
    price = models.PositiveIntegerField(_('price'),)


    def __str__(self):
        return f"{self.name} {str(self.price)}"
    class Meta:
        verbose_name = "Xizmat kursatish turlari"


class Room(models.Model):
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(_('price'), )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Xona turlari"


class Order(models.Model):
    # ServiceChoices = (
    #     ('suv', 'suv'),
    #     ('gaz', 'gaz')
    # )
    roomname = models.CharField(max_length=100, blank=True, null=True)
    roomprice = models.PositiveIntegerField()
    service = models.ManyToManyField(Service, blank=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    #masalanda mana
    #service = models.CharField(max_length=200, choiches=SerciceChoices)
    
    def __str__(self):
        return f"{str(self.roomname)} {str(self.roomprice)}"

class Orders(models.Model):
    roomname = models.CharField(max_length=100, blank=True, null=True)
    roomprice = models.PositiveIntegerField()
    servicename = models.CharField(max_length=100, blank=True, null=True)
    serviceprice = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{str(self.roomname)} {str(self.roomprice)}"

    
class OrderItem(models.Model):
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, related_name='order_one_room')
    service = models.ManyToManyField(Service, blank=True)