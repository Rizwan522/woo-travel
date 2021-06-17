from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 
def bookyourmotorbike(request):
    return render(request,'bookyourmotorbike.html')

def carbooking(request):
    return render(request,'carbooking.html')
  
def busbooking(request):
    return render(request,'busbooking.html')

def Map(request):
    return render(request,'Map.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def kedarnath(request):
    return render(request,'kedarnath.html')

def ladakh(request):
    return render(request,'ladakh.html')

def prayagraj(request):
    return render(request,'prayagraj.html')

def goa(request):
    return render(request,'goa.html')

def manali(request):
    return render(request,'manali.html')

def varanshi(request):
    return render(request,'varanshi.html')

def agra(request):
    return render(request,'agra.html')

def jammu(request):
    return render(request,'jammu.html')

def tirupati(request):
    return render(request,'tirupati.html')

def destinationfortatstar1(request):
    return render(request,'destinationfortatstar1.html')
    
def TataStarbusUltraCitydestination(request):
    return render(request,'TataStarbusUltraCitydestination.html')

def Tatabus1pricebplGoa(request):
    return render(request,'Tatabus1pricebplGoa.html')
   
def tatabus2pricingbplgoa(request):
    return render(request,'tatabus2pricingbplgoa.html')
    
    

