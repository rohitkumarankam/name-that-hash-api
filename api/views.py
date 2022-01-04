from django.shortcuts import HttpResponse
from name_that_hash import runner
import base64

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>welcome to Name-That-Hash api</h1>
        <p>to use that api send http request to http://nth.rka.li/<hash></p>
        <p>example <a href="http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99">http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99</a></p>""")
def hash(request, hash):
    base64str = base64.b64encode(hash.encode('utf-8'))
    hasharray = [str(base64str.decode('utf-8'))]
    output = runner.api_return_hashes_as_json(hasharray, {"base64": True ,"popular_only": True})
    return HttpResponse(output, headers={"Content-Type": "application/json"})