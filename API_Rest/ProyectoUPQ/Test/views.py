import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from WebDevP1.Logica import test


# Create your views here.

@csrf_exempt
def index(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    try:
        nick_name = body['nick_name']
        full_name = body['full_name']
        created = test.create_user(nick_name, full_name)
        response = {
            "status": "successful",
            "code": 200,
            "data": created
        }
    except Exception as err:
        response = {
            "status": "error",
            "code": 200,
            "data": err
        }

    return JsonResponse(response)
