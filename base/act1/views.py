from django.shortcuts import render
from act1.models import Employee
from . import forms

def employeeData(request):
    empleados=Employee.objects.all()
    data={'empleados':empleados}
    return render(request,'act1/empleados.html',data)


# Create your views here.
def userRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=form.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form es valido")
            print("Nombre: ",form.cleaned_data['nombre'])
            print("Email: ",form.cleaned_data['email'])
            print("Fono: ",form.cleaned_data['fono'])
    data={'form':form}
    return render(request,'act1/userRegistration.html',data)