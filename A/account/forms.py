from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile

class UserRegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'kevin'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm your password'}))



    def clean_username(self):
        username=self.cleaned_data['username']
        user=User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('this username already existed')
            # self.add_error('username', 'This username already exists')
        return username
    

    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('this email already existed')
            # self.add_error('email', 'This username already exists')
        return email
    
    def clean(self):
        cd=super().clean()
        p1=cd.get('password')
        p2=cd.get('confirm_password')
        if p1 and p2 and p1 != p2:
            # raise ValidationError('passwords do not match')
            self.add_error('confirm_password', 'Passwords do not match')
        return cd
    
class UserLoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'kevin'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'your password'}))


class EditUserForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Profile
        fields=['age','bio']