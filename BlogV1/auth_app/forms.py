
from django import forms
from django.contrib.auth import (authenticate,get_user_model,login)
from django.contrib.auth.models import User

User=get_user_model()

#################################################################

class UserLoginForm(forms.Form):

    class Meta:
        model = User
        fields = [

            'username',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'id': 'username',
                'required': True,
                'placeholder': 'username',
                'class': "form-control"
            }),

            'password': forms.PasswordInput(attrs={
                'id': 'password',
                'required': True,
                'placeholder': 'password',
                'class': "form-control"
            }),
        }

    def clean(self, *args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        if username and password:
            User = authenticate(username=username, password=password)

            if not User:
                raise forms.ValidationError("this user not exist")
            if not User.check_password(password):
                raise forms.ValidationError("incorrect password")

        return super(UserLoginForm , self).clean(*args,**kwargs)

###################################################################

class UserRegForm(forms.ModelForm):
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': True,
                                                                    'class': "form-control",
                                                                    'placeholder': "password"}))
    cpassword = forms.CharField(label='', widget=forms.PasswordInput(attrs={'required': True,
                                                                    'class': "form-control",
                                                                    'placeholder': "confirm password"}))
    class Meta:

        model=User
        fields=[
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'cpassword'
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'required': True,
                'class': "form-control",
                'placeholder': "first name"
            }),

            'last_name': forms.TextInput(attrs={
                'required': True,
                'class': "form-control",
                'placeholder': "last name"
            }),

            'username': forms.TextInput(attrs={
                'required': True,
                'class': "form-control",
                'placeholder': "username"
            }),

            'email': forms.EmailInput(attrs={
                'required': True,
                'class': "form-control",
                'placeholder': "email"
            }),

        }

        labels = {
            'first_name': '',
            'last_name': '',
            'username': '',
            'email': '',

        }


    def clean_cpassword(self):
        password=self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')

        if password!=cpassword :
            raise forms.ValidationError("Password must match")

        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('Email addresses must be unique.')
        return email
