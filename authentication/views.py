from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('Hello! Welcome to my World!')

def home(request):
    data = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Page Title</title>
            </head>
            <body>
                <h1>Welcome to PySpiders!</h1>
                <marquee>Welcome to Django!</marquee>
            </body>
        </html>"""

    return HttpResponse(data)

def welcome(request):
    with open(r'''D:\QSpiders PySpiders Online Classes\Django\Codes\aProject1_3\authentication\home.html''','r') as file:
        a = file.read()
    return HttpResponse(a)

def demo(request):
    return render(request,'demo.html')