from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World")

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})
