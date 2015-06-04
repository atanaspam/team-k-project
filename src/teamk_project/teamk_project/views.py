from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm#, PasswordChangeForm
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.models import User, Group
from bookingsystem.forms import RegisterForm, EditUserPersonalDetailsForm, loginForm, UserEditDetailsForm

# User Login
def login(request):
    # If the user is logger in already, return a overview page
    # Else return the login page
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

# Invalid
def invalid(request):
    # If the user is authenticated, return the overview page
    # Else the invalid page
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

# Login
def login(request):
    context = RequestContext(request)
    context_dict ={}
    # Check if request if post and secure
    if request.method == 'POST':
        form = loginForm(request.POST)
        # Validate form
        if form.is_valid():
            # Get data from form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Get user
            user = auth.authenticate(username=username, password=password)
            # If user exists and is active, return overview page and
            # authenticate the user
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
            print form.errors
    else:
        form = loginForm()
    return render_to_response('login.html', {'form':form}, context)

# Register
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
            # Redirect on success
            return redirect('/success.html')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = RegisterForm()
    return render_to_response('register.html', {'form': form}, context)

# Edit profile
@login_required
def editProfile(request):

    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}

    if request.method == 'POST':
        form = UserEditDetailsForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            print form
    else:
        # If the request was not a POST, display the form to enter details.
        form = UserEditDetailsForm(initial={'telephone':user.additionalinfo.telephone, 'email':user.email })
        context['form'] = form
        print form
    return render_to_response('editProfile.html', context_dict, context)

# Logout
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

# Success
def success(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('success.html', context_dict, context)

# Embedded Success
def successEmb(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('successEmb.html', context_dict, context)

# Fail
def fail(request):
    context = RequestContext(request)
    context_dict={}
    return render_to_response('fail.html', context_dict, context)

# Index
def index(request):
    context = RequestContext(request)
    user = request.user
    print user
    context_dict = {'user':user}
    return render_to_response('index.html', context_dict, context)


# Currently unused

def about(request):
    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}
    return render_to_response('about.html', context_dict, context)

def ageGroups(request):
    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}
    return render_to_response('ageGroups.html', context_dict, context)

def contact(request):
    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}
    return render_to_response('contact.html', context_dict, context)

def events(request):
    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}
    return render_to_response('events.html', context_dict, context)

def news(request):
    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}
    return render_to_response('news.html', context_dict, context)