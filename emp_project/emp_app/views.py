from django.shortcuts import render, get_object_or_404
from .models import employee
from .serializer import EmployeeSerializer
from rest_framework import generics
import requests
from . import forms
# Create your views here.

def index_view(request):
    form=forms.EmployeeRegistration()
    Employees=employee.objects.all()
    return render(request,'emp_app/index.html',{'Employees':Employees,'form':form})

class Employee_data(generics.ListCreateAPIView):
    queryset=employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_fields = ('eno', 'ename', 'esal', 'eaddr')
