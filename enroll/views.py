from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .forms import StudentsRegistration
from .models import User

# Create your views here.
def home(request):
    if request.method == "POST":
        fm = StudentsRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pss = fm.cleaned_data['password']
            reg = User(name=name, email=email, password=pss)
            reg.save()
            fm = StudentsRegistration()
            return redirect('home')
    else:
        fm = StudentsRegistration()
    stud = User.objects.all()
    return render(request, 'home.html', {'form':fm, 'std':stud})

def delete(request, uid):
    User.objects.get(pk=uid).delete()
    return redirect('home')


def update(request, uid):
    if request.method == "POST":
        dt = User.objects.get(pk=uid)
        fm = StudentsRegistration(request.POST, instance=dt)
        if fm.is_valid():
            fm.save()
        return redirect('home')
    else:
        dt = User.objects.get(pk=uid)
        fm = StudentsRegistration(instance=dt)
    return render(request, 'update.html', {'form':fm})
