from django.db import models
from django.urls import reverse
from Customeruser.models import CustomBaseuser
from roomapp.models import RoomModel
from guestpreferenceapp.models import Preferencemodel
from Payment.models import PaymentModel
import datetime

# Create your models here.

class StateModel(models.Model):
    user=models.OneToOneField(CustomBaseuser,on_delete=models.CASCADE)
    checkInDateandTime= models.DateTimeField(null=False,blank=False)
    numberofdays = models.CharField(max_length=150, blank=False,null=True)
    room = models.CharField(max_length=150, blank=False,null=True)
    def __str__(self):
        return f'{self.user} State'
        

class ReservationModel(models.Model):
    user=models.ForeignKey(CustomBaseuser,on_delete=models.CASCADE)
    checkInDateandTime= models.DateTimeField(null=False,blank=False)
    preference=models.ForeignKey(Preferencemodel,on_delete=models.CASCADE,null=True)
    numberofdays = models.CharField(max_length=150, blank=False,null=True)
    payment=models.OneToOneField(PaymentModel,on_delete=models.CASCADE,null=True,blank=True)
    room = models.CharField(max_length=150, blank=False,null=True)
    def __str__(self):
        return f'{self.checkInDateandTime} {self.user.email} Reservation'
    
    def checkoutime(self):
        time = self.checkInDateandTime + datetime.timedelta(days=int(self.numberofdays))
        return time
    def getabsoluteurl(self):
        return reverse('reservation_id',kwargs={"id":self.id})

class ReservedRooms(models.Model):
    reservedroom=models.ForeignKey(ReservationModel, on_delete=models.CASCADE)
    room=models.OneToOneField(RoomModel,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.room.roomname}'