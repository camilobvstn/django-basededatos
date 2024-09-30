from django.shortcuts import render
from act1.models import Employee


def employeeData(request):
    empleados=Employee.objects.all()
    data={'empleados':empleados}
    return render(request,'act1/empleados.html',data)
# Create your views here.
