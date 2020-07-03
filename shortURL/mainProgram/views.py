from django.shortcuts import render,reverse,redirect, get_object_or_404
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

def redirectView(request,pk):
    url_id = fromBase62(pk)
    fullURL = get_object_or_404(StoreURL,id = url_id)
    return redirect(str(fullURL))
