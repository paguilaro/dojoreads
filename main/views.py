from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from .models import Authors

@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


@login_required
def revision(request):
    authors = Authors.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'new_revision.html', context)
    