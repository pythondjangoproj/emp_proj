from django.contrib import admin
from .models import employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

# Register your models here.
admin.site.register(employee,EmployeeAdmin)