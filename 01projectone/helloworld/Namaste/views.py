from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def another(request):
    return HttpResponse('Namaste means Hello in Hindi')
