from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница</h1>")

def data(request):
    text_html = "<h1>Это  страница дата</h1> <p> Это параграф </p>  <p> Это второй параграф </p>"
    return HttpResponse(text_html)

def test(request):
    return HttpResponse("<h1>Это  страница тест</h1> <p> Тут должно что-то быть </p> ")