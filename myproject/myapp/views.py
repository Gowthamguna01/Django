from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging

# Create your views here.
posts = [
        {'id':1, 'title': 'post 1', 'content': 'content of post 1'},
        {'id':2, 'title': 'post 2', 'content': 'content of post 2'},
        {'id':3, 'title': 'post 3', 'content': 'content of post 3'},
        {'id':4, 'title': 'post 4', 'content': 'content of post 4'},
    ]

def morning(request):
    return HttpResponse("<h1>hello everyone iam gowtham..!</h1>")


def num(request, val):
    return HttpResponse(f"connected.. This is a number response= {val}")

def sentence(request, letter):
    return HttpResponse(f"this is a sentence, {letter}")

def old_url(request):
    return redirect(new_url)

def new_url(request):
    return HttpResponse('connected this is new url')

def old_page_url(request):
    return redirect(reverse("myapp:newreverse"))

def new_page_url(request):
    return HttpResponse("hi this is reverse method.. ")

def index(request):
    blog_title = "G vlogs"
    
    return render(request, 'index.html', {'blog_title': blog_title, 'posts':posts})

def detail(request, blog_id):
    post = next((item for item in posts if item['id'] == blog_id), None)
    logger = logging.getLogger("TESTING")
    logger.debug(f'post variable is {post}')
    return render(request, 'detail.html', {'post': post})