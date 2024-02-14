# from django.shortcuts import render
# from django.shortcuts import render
import random
import string
from django.http import JsonResponse
import requests
import json
from django.shortcuts import HttpResponse
from django.core.cache import cache

# Create your views here.

# Random values function
def random_data(num_records):
     

   data = []
   print(num_records)
   for _ in range(num_records):
       first_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 10)))
       last_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(3, 10)))
       email = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))) + '@gmail.com'
       age = random.randint(18, 80)
       phone_number = ''.join(random.choices(string.digits, k=10))

       record = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'age': age,
            'phone_number': phone_number
        }
    #    record = {
    #         'ttttttest': 123,
    #     }
       data.append(record)
#    print(num_records)
   return data
   
def set_cache_data(request):
    try:
        num_records = int(request.GET.get('num_records', 100))
        generated_data = random_data(num_records)
        cache.set('test',generated_data,timeout=3600 )
        return JsonResponse(generated_data, safe=False)
    except Exception as e:
        print(e)
        return HttpResponse(e)

def fetch_cached_data(request):
    set_cache_data(request)
    cache_data = cache.get('test')
    # generated_data = random_data(num_records)
    # print(generated_data)
    if cache_data:
        return JsonResponse(cache_data, safe=False)
    
    
       