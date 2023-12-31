from django.db import models


# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    
    
    def __str__(self):
        return f"{self.id}: {self.code} : {self.city}"
    
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.id} : from {self.origin} to {self.destination} , duration : {self.duration} "
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration >= 0
    
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers" )
    
    def __str__(self):
        return f"{self.first} {self.last}"