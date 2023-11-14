from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            # Acción a realizar con los datos del formulario
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            acceso_timestamp = formulario.cleaned_data['acceso_timestamp']

            # Aquí puedes realizar la lógica de autenticación, guardar el acceso en la base de datos, etc.

            return render(request, 'repaso/index.html', {'formulario': formulario})
    else:
        formulario = LoginForm()

    return render(request, 'repaso/index.html', {'formulario': formulario})