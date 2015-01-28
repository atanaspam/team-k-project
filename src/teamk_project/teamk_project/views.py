from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def login(request):
    if request.user.is_authenticated():
        if request.user.groups.filter(name = 'Manager'):
            return HttpResponseRedirect("/bookingsystem/manager/")
        elif request.user.groups.filter(name = 'Coach'):
            return HttpResponseRedirect("/bookingsystem/coach/")
        elif request.user.groups.filter(name = 'Parent'):
            return HttpResponseRedirect("/bookingsystem/parent/")
        else:
            return HttpResponseRedirect("/")
    else:
        return render(request, "login.html")
        
def invalid(request):
    if request.user.is_authenticated():
        if request.user.groups.filter(name = 'Manager'):
            return HttpResponseRedirect("/bookingsystem/manager/")
        elif request.user.groups.filter(name = 'Coach'):
            return HttpResponseRedirect("/bookingsystem/coach/")
        elif request.user.groups.filter(name = 'Parent'):
            return HttpResponseRedirect("/bookingsystem/parent/")
        else:
            return HttpResponseRedirect("/")
    else:
        return render(request, "invalid.html")


def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)    
    if user:
        if user.is_active:
            auth.login(request, user)
            if user.groups.filter(name = 'Manager'):
                return HttpResponseRedirect("/bookingsystem/manager/")
            elif user.groups.filter(name = 'Coach'):
                return HttpResponseRedirect("/bookingsystem/coach/")
            elif user.groups.filter(name = 'Parent'):
                return HttpResponseRedirect("/bookingsystem/parent/")
            else:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("This Account is Disabled")
    else:
        # Invalid details. Incorrect Username/Password
        return HttpResponseRedirect("/invalid.html")
            
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")