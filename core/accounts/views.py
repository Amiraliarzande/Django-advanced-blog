from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sendEmail
from django.core.cache import cache
from django.views.decorators.cache import cache_page
import requests
from django.http import JsonResponse
# Create your views here.

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>done</h1>")

@cache_page(10)
def test(request):

    try:
        
        response = requests.get("https://saffronhaddad.ir/")
        text_content = response.text
        
        data = {
            "saved_email": "info@saffronhaddad.ir" if "info@saffronhaddad.ir" in text_content else "",
            "saved_phone": "09151712200" if "09151712200" in text_content else ""
        }

        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)