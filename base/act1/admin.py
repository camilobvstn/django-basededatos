from django.contrib import admin
from act1.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['nombre','email','fono']

admin.site.register(Employee,EmployeeAdmin)
