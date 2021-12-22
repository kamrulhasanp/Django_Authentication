from django.contrib import auth
from django.urls import reverse_lazy
from django.contrib.messages import success
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from . forms import RegisterForm


# Create your views here.

def index(request):

    return render( request, 'index.html')


def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
      
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('index')

        

    context = {'form':form}

    return render(request, 'registration/register.html', context )

def logout(request):
    auth.logout(request)
    return redirect('index')

class PasswordsChangeView(PasswordChangeView):
    form_clsass = PasswordChangeForm

    success_url = reverse_lazy('index')

