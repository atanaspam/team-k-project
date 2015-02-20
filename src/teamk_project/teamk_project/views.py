from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from bookingsystem.forms import RegisterForm
from django.contrib.auth.models import User, Group

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
            return HttpResponseRedirect("This Account is Disabled. Please contact support!")
    else:
        context = RequestContext(request)
    	context_dict={}
        context_dict["passed"] = "False"
    	return HttpResponseRedirect('/invalid.html')

def register(request):
    context = RequestContext(request)
    # A HTTP POST?
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            user=form.save(commit=False)
            #user.blockid = getLastBlockID()
            newUser = User.objects.create_user(user.username, user.email, user.password)
            newUser.first_name = user.first_name
            newUser.last_name = user.last_name
            g = Group.objects.get(name='Parent')
            g.user_set.add(newUser)
            newUser.save()
            #   print user.username
            # Redirect on success
            return redirect('/success.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def success(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('success.html', context_dict, context)

def successEmb(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('successEmb.html', context_dict, context)


def fail(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('fail.html', context_dict, context)