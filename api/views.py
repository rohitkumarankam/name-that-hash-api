from django.shortcuts import HttpResponse
from name_that_hash import runner
import base64

# Create your views here.
def index(request):
    return HttpResponse("""
        <h1>welcome to Name-That-Hash api</h1>
        <p>to use the api send http GET request to http://nth.rka.li/&lt;base64 encoded hash&gt;</p>
        <p>example <a href="http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99">http://nth.rka.li/2d235ace000a3ad85f590e321c89bb99</a></p>

        <input type="text" name="hash" placeholder="hash" id="hash">
        <button type="submit" onclick="search();">search with api</button>
        <button type="submit" onclick="searchgui();">search with gui</button>
        <script type="text/javascript">
        let hashtext = document.getElementById("hash");
        function search() {
            console.log(btoa(hashtext.value));
            location.assign(window.location.origin + "/" + btoa(hashtext.value));
        }
        function searchgui() {
            location.assign(window.location.origin +"/"+ btoa(hashtext.value) +"/view");
        }
        </script>
        """)
def hash(request, hash):
    txt = [str(hash),]
    output = runner.api_return_hashes_as_json(txt, {"base64": True ,"popular_only": True})
    return HttpResponse(output, headers={"Content-Type": "application/json"})

def view(request, hash):
    txt = [str(hash),]
    output = runner.api_return_hashes_as_dict(txt, {"base64": True ,"popular_only": True})
    style = """
    <style>
    table, th, td {
        border:1px solid black;
    }
    </style>
    """
    response= ""#<th>extended</th>    txt = [str(hash),]
    hashtxt = str(list(output.keys())[0])
    hashout= output.get(hashtxt)
    response += "<h2>Hash: "+ hashtxt +"</h2>"
    if (len(list(hashout)) > 0):
        response += "<table><tr><th>Name</th><th>hashcat</th><th>john</th><th>description</th></tr>"
        for i in hashout:
            response += "<tr>"
            response += "<th>" + str(i.get("name")) + "</th>"
            response += "<th>" + str(i.get("hashcat")) + "</th>"
            response += "<th>" + str(i.get("john")) + "</th>"
            # response += "<th>" + str(i.get("extended")) + "</th>"
            response += "<th>" + str(i.get("description")) + "</th>"
            response += "</tr>"
            a = "a"
        response += "</table>"
    else:
        response += "<h3 style='color:red;''>can't find hashing algorithm</h3>"
    head = "<h1>Name-That-Hash</h1>"
    allres = style+head+response
    return HttpResponse(allres)