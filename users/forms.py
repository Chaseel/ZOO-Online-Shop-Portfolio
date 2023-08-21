from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-group", 'placeholder' : 'Введите ваше имя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-group", 'placeholder' : 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username','password',)

class UserRegistrForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "form-group", 'placeholder' : 'Введите ваше имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : "form-group", 'placeholder' : 'example@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-group", 'placeholder' : 'Введите ваш пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class' : "form-group", 'placeholder' : 'Повторите ваш пароль'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : "form-group", 'placeholder' : 'Аватар'}), required=False)



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'image')

class UserProfileForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : "user-info", 'readonly' : True}))   
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class' : "user-info", 'readonly' : True}))     
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class' : "save-button"}), required=False)  
    about_us = forms.CharField(widget=forms.Textarea(attrs={
        'class' : "user-bio"}))        
    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'about_us')        