import re
import datetime
from django.utils import timezone
from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', initial='')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, initial='')
    #acceso_timestamp = forms.CharField(widget=forms.HiddenInput, initial=timezone.now())

    def clean_username(self):
        username = self.cleaned_data['username']
        # Ejemplo de validación: asegurarse de que el nombre de usuario no contenga caracteres especiales
        if not username.isalnum():
            raise ValidationError('El nombre de usuario no debe contener caracteres especiales.')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        username = self.cleaned_data.get('username')

        # Validación de la longitud mínima
        if len(password) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')

        # Validación de al menos un carácter especial, un número y letras mayúsculas y minúsculas
        elif not any(char.isdigit() for char in password):
            raise ValidationError(
                'La contraseña debe contener al menos un número.')
        elif not any(char.islower() for char in password):
            raise ValidationError(
                'La contraseña debe contener al menos una minúscula.')
        elif not any(char.isupper() for char in password):
            raise ValidationError(
                'La contraseña debe contener al menos una mayúscula.')
        elif not any(char.isalnum() for char in password):
            raise ValidationError(
                'La contraseña debe contener al menos un carácter especial.')
        elif username and password.lower() in username.lower():
            raise ValidationError('La contraseña no debe contener el nombre de usuario.')
        else:
            raise ValidationError(
                'Login realizado con exito'
            )

        # Validación la contraseña no debe contener el nombre de usuario

        return password


