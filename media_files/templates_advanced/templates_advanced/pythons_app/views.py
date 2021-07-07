from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


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
