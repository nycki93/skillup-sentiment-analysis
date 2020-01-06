from django.shortcuts import render
from django.http import HttpResponse


def index(request) -> HttpResponse:
    
    return HttpResponse(
        "<h1>Hello, world. You're at the app index.</h1>"
    )

def parrot(request, query) -> HttpResponse:
    return HttpResponse(
        "Your query was: " + query
    )
