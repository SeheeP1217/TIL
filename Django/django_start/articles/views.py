from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def index(request):
    print("here")
    #return HttpResponse("<h1>hola</h1>")
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'orange', 'banana']
    info = {'name':'SEHEE'}
    context = {
        'foods': foods,
        'info': info
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['초밥', '아이스아메리카노', '쿠키', '티즐']
    pick = random.choice(foods)
    context = {
        'foods': foods,
        'pick': pick

    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {'data': data}
    return render(request, 'articles/catch.html')

def fake_google(request):
    return render(request, 'articles/fake-google.html')

def hello(request, name):
    context = {'name' : name}
    return render(request, 'articles/hello.html', context)