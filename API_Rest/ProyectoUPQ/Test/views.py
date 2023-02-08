from django.shortcuts import render
from django.http import JsonResponse
from P1.Logica import test

# Create your views here.

def index(Request):
    responce = {
        "status": "successful",
        "code": 200,
        "data": test.funcion()
    }
    return JsonResponse(responce)