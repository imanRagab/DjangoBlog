
from django import forms
from django.contrib.auth import (authenticate,get_user_model,login)


User=get_user_model()

class UserLoginForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField()

    def clean(self, *args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        if username and password:
            User = authenticate(username=username, password=password)

            if not User:
                raise forms.ValidationError("this user noy exist")
            if not User.check_password(password):
                raise forms.ValidationError("incorrect password")

        return super(UserLoginForm , self).clean(*args,**kwargs)







