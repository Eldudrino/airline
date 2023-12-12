from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from .models import Flight, Airport , Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=int(flight_id))
    
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights = flight)
    })
    
    
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))
    
def cancel(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.remove(flight)
        return HttpResponseRedirect(reverse('flight', args=(flight_id,)))

    
