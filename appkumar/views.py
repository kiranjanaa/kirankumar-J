from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ganesh(request):
    return HttpResponse('my friend name is ganesh')
def ramesh(request):
    return HttpResponse('<h1>my name is ramesh<h1>')
def ram(request):
    return HttpResponse('<marquee> my name is ram</marquee>')

def mani(request):
    return HttpResponse('<h1>mani is my friend</h1><img src="https://png.pngtree.com/thumb_back/fh260/background/20230411/pngtree-nature-forest-sun-ecology-image_2256183.jpg">')