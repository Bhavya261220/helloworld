from django.http import JsonResponse
from django.shortcuts import render

from django.http import HttpResponse

def hello_html(request):
    html_content = "<html><head><title>Hello World</title></head><body><b>Hello World!</b></body></html>"
    return HttpResponse(html_content)
def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

