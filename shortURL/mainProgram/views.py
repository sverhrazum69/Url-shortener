from django.shortcuts import render
from django.http import HttpResponse

from .encoder import toBase62, fromBase62

def hello(request):
    print(toBase62(289))
    return HttpResponse(fromBase62('F4'))

