from django.shortcuts import render,reverse
from django.http import HttpResponse
from .models import StoreURL

from .encoder import toBase62, fromBase62

def mainPage(request):
    context = {}
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        StoreURL.objects.create(url = original_url)
        id = StoreURL.objects.latest('id').id
        shortUrl = request.get_host() + '/' + toBase62(id)

        context = {'shortUrl':shortUrl}

    return render(request,'mainProgram/main.html',context)

