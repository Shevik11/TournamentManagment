from django.shortcuts import render
from .forms import RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view


# Create your views here.
# Створення функції для реєстрації користувача
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')  # Перенаправлення на головну сторінку після реєстрації
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})