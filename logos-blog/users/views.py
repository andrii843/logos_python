from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from users.models import User
from users.forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.http import Http404


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newuser = User()
            newuser.username = data['username'],
            newuser.password = make_password(data['password'])
            newuser.save()
            return redirect('/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'users/register.html', context)
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'users/register.html', context)


def auth(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return Http404("User not found")
    else:
        return render(request, 'users/auth.html')
