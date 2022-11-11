from django.db import models









class ServiceType(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.name} {str(self.price)}"
    class Meta:
        verbose_name = "ServiceType"

class RoomCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xona turlari"


class Orders(models.Model):
    roomname = models.CharField(max_length=100)
    roomprice = models.PositiveIntegerField()
    servicename = models.CharField(max_length=100)
    serviceprice = models.PositiveIntegerField()
    def __str__(self):
        return f"{str(self.roomname)} {str(self.roomprice)}"