"""
URL configuration for dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.home, name='home'),
    path('addStudent',index.addstud, name='addstud'),
    path('classSched',index.classsched, name='classsched'),
    path('editStudent',index.editstud, name='editstud'),
    path('payment',index.payment, name='payment'),
    path('studentReg',index.studreg, name='studreg'),
    path('studentInfo',index.teach1studinfo, name='teach1studinfo'),
    path('assignSched',index.teachclasssched, name='teachclasssched'),
    path('studentList',index.teachstudlist, name='teachstudlist'),
    path('uploadPay',index.uploadpay, name='uploadpay'),
    path('studentInfoParent', index.stud1info, name='stud1info'),
    path('assignStudent',index.teachclassassign, name='teachclassassign'),
]
