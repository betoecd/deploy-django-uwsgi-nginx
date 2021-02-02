from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'host_header': request.META['HTTP_HOST'],
        'bits': '10 bilhões por cento de certeza!!!',
    })
