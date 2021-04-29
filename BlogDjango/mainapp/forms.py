from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    #aqui podemos customizar los fields
    #y añadir placeholder

    password1 = forms.CharField(label="Contraseña",
    widget=forms.PasswordInput(
         attrs={
            'placeholder': 'Contraseña',
            'class':'form-control'
         })
    )
    password2 = forms.CharField(label="Repetir contraseña",
    widget=forms.PasswordInput(
         attrs={
            'placeholder': 'Repetir contraseña',
            'class':'form-control'
         })
    )
    
    class Meta:
        model = User
        #aqui podemos meter opciones como el placeholder si no hemos definido el field anteriormente
        widgets = {
            'username' : forms.TextInput(attrs = {'placeholder': 'Usuario', 'class':'form-control'}),
            'email'    : forms.TextInput(attrs = {'placeholder': 'E-Mail', 'class':'form-control'}),
            'first_name'    : forms.TextInput(attrs = {'placeholder': 'Nombre', 'class':'form-control'}),
            'last_name'    : forms.TextInput(attrs = {'placeholder': 'Apellidos', 'class':'form-control'}),
        }
        #aqui hay que añadir los fields que queremos en el formulario
        fields = ['username','email','first_name','last_name', 'password1', 'password2']
    