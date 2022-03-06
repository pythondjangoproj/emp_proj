from django.contrib import admin
from django.urls import path
from emp_app import views

app_name='emp_app'
urlpatterns = [
    path('',views.index_view, name='index_view'),
    path('api/',views.Employee_data.as_view()),
]
