from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request,'index.html',)

def pricing(request):
    return render(request,'pricing.html',) 

def aboutus(request):
    return render(request,'aboutus.html',)          

def contactus(request):
    return render(request,'contactus.html',)          