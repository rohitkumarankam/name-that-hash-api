from django.shortcuts import HttpResponse
from name_that_hash import runner

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>welcome to Name-That-Hash api</h1>
        <p>to use that api send http request to http://nth.rka.li/<hash></p>
        <p>example <a href="http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99">http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99</a></p>""")
def hash(request, hash):
    hashes = [str(hash)]
    output = runner.api_return_hashes_as_json(hashes, {"popular_only": True})
    return HttpResponse(output)