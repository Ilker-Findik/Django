from django.shortcuts import render
from .models import Kategoriler,Markalar,Urunler,Etiketler

# Create your views here.

def anasayfa(request):
    urunler=Urunler.objects.filter(anasayfa=True)
    return render(request, 'index.html',{'urunler':urunler})

def basarizliklarim(request):
    return render(request, 'basarisizliklarim.html')