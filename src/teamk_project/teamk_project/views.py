from django import forms
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from bookingsystem.forms import RegisterForm, EditUserPersonalDetailsForm, loginForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import PasswordChangeForm

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


def login(request):
    context = RequestContext(request)
    context_dict ={}
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
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
            print form.errors
    else:
        form = loginForm()
    return render_to_response('login.html', {'form':form}, context)

    # username = request.POST.get('username', '')
    # password = request.POST.get('password', '')
    # user = auth.authenticate(username=username, password=password)
    # if user:
    #     if user.is_active:
    #         auth.login(request, user)
    #         if user.groups.filter(name = 'Manager'):
    #             return HttpResponseRedirect("/bookingsystem/manager/")
    #         elif user.groups.filter(name = 'Coach'):
    #             return HttpResponseRedirect("/bookingsystem/coach/")
    #         elif user.groups.filter(name = 'Parent'):
    #             return HttpResponseRedirect("/bookingsystem/parent/")
    #         else:
    #             return HttpResponseRedirect("/")
    #     else:
    #         return HttpResponseRedirect("This Account is Disabled. Please contact support!")
    # else:
    #     context = RequestContext(request)
    # 	context_dict={}
    #     context_dict["passed"] = "False"
    # 	return HttpResponseRedirect('/invalid.html')

    # context = RequestContext(request)
    # form = CreateChildForm(initial={})
    # context_dict = {'parent': request.user}
    # #print lastID
    # if request.method == 'POST':
    #     form = CreateChildForm(request.POST)
    #     # Have we been provided with a valid form?
    #     if form.is_valid():
    #         child=form.save(commit=False)
    #         child.uid = getLastID
    #         child.ismember = 0
    #         child.belongsto = request.user
    #         child.experiencelevel=0
    #         child.save()
    #         # Redirect on success
    #         return redirect('/success.html')
    # # If the request was not a POST, display the form to enter details.
    # context_dict['form'] = form
    # return render_to_response('parent/addNewChild.html', context_dict, context)

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

def editProfile(request):

    context = RequestContext(request)
    user = request.user
    context_dict = {'user':user}

    if "/manager/" in request.META.get('HTTP_REFERER'):
        context_dict['sidebar'] = "manager"
    elif "/coach/" in request.META.get('HTTP_REFERER'):
        context_dict['sidebar'] = "coach"
    elif "/parent/" in request.META.get('HTTP_REFERER'):
        context_dict['sidebar'] = "parent"

    if request.method == 'POST':
        form = EditUserPersonalDetailsForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            print form
    else:
        # If the request was not a POST, display the form to enter details.
        form = EditUserPersonalDetailsForm()
        context['form'] = form
    return render_to_response('editProfile.html', context_dict, context)

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

def index(request):
    context = RequestContext(request)
    user = request.user
    print user
    context_dict = {'user':user}
    return render_to_response('index.html', context_dict, context)