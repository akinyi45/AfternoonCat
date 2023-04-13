from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm


def blog(request):
    return render(request, 'blog.html')

def single(request):
    return render(request, 'single.html')

def index(request):
    return render(request, 'index.html')

def portfolio(request):
    return render(request, 'portfolio.html')




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.save()
            messages.success(request, f'Account created for{username}')
            return redirect('user-registration')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})
