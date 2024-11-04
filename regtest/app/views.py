from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
        if request.method=="post":
            name=request.POST['name']
            email=request.POST['email']
            dob=request.POST['dob']
            gender=request.POST['gender']
            stuClass=request.POST['classname']
            reg=request.POST['reg']
            test=request.POST['test']

            print("name is", name,email,dob,gender,stuClass,reg,test)
            return render(request,'index.html')

        return render(request,'index.html')