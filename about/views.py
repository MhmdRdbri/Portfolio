from django.shortcuts import render
from .models import *

def about(request):
    abouts = About.objects.all()

    return render(request, '')