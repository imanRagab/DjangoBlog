
from django.contrib.auth import (authenticate,login)
from forms import UserLoginForm, UserRegForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

########################################################################

def register_view(request):
    title = "Register"
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/ourblog/home')

    context = {
        "form": form,
        "title": title
    }
    return render(request, 'register.html', context)


####################################################

def login_view(request):
    login_form = UserLoginForm(request.POST or None)
    context = {'login_form': login_form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/ourblog/home')
            else:
                return HttpResponse("Your account has been blocked please contact the admin")

        else:
            return HttpResponse("user with this data is not found")

    return render(request, 'login.html', context)


#####################################################


def logout_view(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])
