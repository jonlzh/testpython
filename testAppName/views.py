from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
# Create your views here.
def index(request):
    return render(request, 'testAppName/index.html')