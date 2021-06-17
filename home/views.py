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

def Tatab3d(request):
    return render(request,'Tatab3d.html')

def Tatab3pricebplgoa(request):
    return render(request,'Tatab3pricebplgoa.html')

def Volvob1d(request):
    return render(request,'Volvob1d.html')

def Volvob2d(request):
    return render(request,'Volvob2d.html')

def Volvob3d(request):
    return render(request,'Volvob3d.html')

def Volvob1dpricebplgoa(request):
    return render(request,'Volvob1dpricebplgoa.html')

def Volvob2dpricebplgoa(request):
    return render(request,'Volvob2dpricebplgoa.html')

def Volvob3dpricebplgoa(request):
    return render(request,'Volvob3dpricebplgoa.html')

def MCB1d(request):
    return render(request,'MCB1d.html')

def MCB2d(request):
    return render(request,'MCB2d.html')

def MCB3d(request):
    return render(request,'MCB3d.html')

def MCB1pricebplgoa(request):
    return render(request,'MCB1pricebplgoa.html')

def MCB2pricebplgoa(request):
    return render(request,'MCB2pricebplgoa.html')

def MCB3pricebplgoa(request):
    return render(request,'MCB3pricebplgoa.html')
def Sclb1d(request):
    return render(request,'Sclb1d.html')
def Sclb2d(request):
    return render(request,'Sclb2d.html')
def Sclb3d(request):
    return render(request,'Sclb3d.html')

def Sclb1dpricebplgoa(request):
    return render(request,'Sclb1dpricebplgoa.html')

def Sclb2dpricebplgoa(request):
    return render(request,'Sclb2dpricebplgoa.html')

def Sclb3dpricebplgoa(request):
    return render(request,'Sclb3dpricebplgoa.html')

def payment(request):
    return render(request,'payment.html')

def Sc1d(request):
    return render(request,'Sc1d.html')

def Sc2d(request):
    return render(request,'Sc2d.html')

def Sc3d(request):
    return render(request,'Sc3d.html')

def Sc1pricebplgoa(request):
    return render(request,'Sc1pricebplgoa.html')

def Sc2pricebplgoa(request):
    return render(request,'Sc2pricebplgoa.html')

def Sc3pricebplgoa(request):
    return render(request,'Sc3pricebplgoa.html')

def Asb1d(request):
    return render(request,'Asb1d.html')

def Asb2d(request):
    return render(request,'Asb2d.html')

def Asb1dpricebplgoa(request):
    return render(request,'Asb1dpricebplgoa.html')

def Asb2dpricebplgoa(request):
    return render(request,'Asb2dpricebplgoa.html')
    
def Br1d(request):
    return render(request,'Br1d.html')

def Br1dpricebplgoa(request):
    return render(request,'Br1dpricebplgoa.html')

def Br2d(request):
    return render(request,'Br2d.html')

def Br2dpricebplgoa(request):
    return render(request,'Br2dpricebplgoa.html')

def Br3d(request):
    return render(request,'Br3d.html')

def Br3dpricebplgoa(request):
    return render(request,'Br3dpricebplgoa.html')

    
    

