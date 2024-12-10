from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Birga


# Create your views here.
def hellow_http(request):    
    response_text = "Привет"
    birga = Birga.objects.all()
    results = []
    
    for item in birga: 

        rate = {
                "id": item.id,
                "time": item.time,
                "dollar": item.dollar,
                "evro": item.eBro,
                "tenge": item.tenge,
                "som": item.som,
        }
        results.append(rate)
    
    dictionary = {
            "current": results[0],           
        
        "total": len(birga),
        "results":results                    
    }
    return JsonResponse(dictionary,json_dumps_params={'ensure_ascii':False})

    
  