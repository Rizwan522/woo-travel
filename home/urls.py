from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("carbooking",views.carbooking, name='carbooking'),
    path("busbooking",views.busbooking, name='busbooking'),
    path("bookyourmotorbike",views.bookyourmotorbike, name='bookyourmotorbike'),
    path("Map",views.Map, name='Map'),
    path("kedarnath",views.kedarnath, name='kedarnath'),
    path("ladakh",views.ladakh, name='ladakh'),
    path("prayagraj",views.prayagraj, name='prayagraj'),
    path("goa",views.goa, name='goa'),
    path("manali",views.manali, name='manali'),
    path("varanshi",views.varanshi, name='varanshi'),
    path("agra",views.agra, name='agra'),
    path("jammu",views.jammu, name='jammu'),
    path("tirupati",views.tirupati, name='tirupati'),
    path("destinationfortatstar1",views.destinationfortatstar1, name='destinationfortatstar1'),
    path("Tatabus1pricebplGoa",views.Tatabus1pricebplGoa, name='Tatabus1pricebplGoa'),
    path("TataStarbusUltraCitydestination",views.TataStarbusUltraCitydestination, name='TataStarbusUltraCitydestination'),
    path("tatabus2pricingbplgoa",views. tatabus2pricingbplgoa, name=' tatabus2pricingbplgoa'),
    ]