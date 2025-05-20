# Create your views here.

from django.shortcuts import render, redirect
from .admin import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(request, 'Registrado. Agora faça o login para começar!')
            return redirect('base')

        else:
            print('invalid registration details')
            
    return render(request, "registration/registro.html",{"form": form})