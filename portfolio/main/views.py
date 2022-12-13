from django.shortcuts import render
from .models import Main

def main_index(request):
    return render(request, 'main_index.html')
