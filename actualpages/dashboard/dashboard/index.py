from django.http import HttpResponse
from django.shortcuts import render

def addstud(request):
    return render(request,'addstud.html')

def classsched(request):
    return render(request,'classsched.html')

def editstud(request):
    return render(request,'editstud.html')

def home(request):
    return render(request,'home.html')

def payment(request):
    return render(request,'payment.html')

def studreg(request):
    return render(request,'studreg.html')

def teach1studinfo(request):
    return render(request,'teach1studinfo.html')

def teachclasssched(request):
    return render(request,'teachclasssched.html')

def teachstudlist(request):
    return render(request,'teachstudlist.html')

def uploadpay(request):
    return render(request,'uploadpay.html')

def stud1info(request):
    return render(request,'stud1info.html')

def teachclassassign(request):
    return render(request,'teachclassassign.html')
