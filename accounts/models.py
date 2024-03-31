from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import  datetime

# Create your models here.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,label = "Email" ,error_messages={'Exists': 'this is massage all ready Exists'})
    # fullname = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username",  "email", )
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        # self.fields['fullname'].widget.attrs['placeholder'] = 'fullname'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm_password'


    def save(self, commit=True):

        user = super(RegisterForm, self).save(commit=False)
        # first_name, last_name = self.cleaned_data["fullname"].split()
        # user.first_name = first_name
        # user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

  
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        # user.fullname = self.cleaned_data["fullname"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user