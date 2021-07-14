from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import PythonCreateForm
from .models import Python


# Create your views here.
from ..core.decorators import any_group_required


def sign_in(request):
    user = authenticate(username='ogi', password='alabala123')
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


# @login_required(login_url='/sign-in')
@any_group_required(groups=['User'])
def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
    else:
        form = PythonCreateForm(req.POST, req.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(req, 'create.html', {'form': form})
