
from django.contrib.auth import (authenticate,login)
from django.shortcuts import render
from .forms import UserLoginForm

def login_view(request):
    print (request.User.is_authenticated())
    title="Login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        User=authenticate(username=username,password=password)
        login(request,User)
    print (request.User.is_authenticated())


    return render(request , "form.html", {"form":form,"title":title})



