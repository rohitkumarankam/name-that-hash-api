from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the api index.")
def hash(request, hash):
    return HttpResponse("Hello, world. You're at the api hash."+hash)