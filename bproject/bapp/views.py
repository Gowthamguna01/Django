from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bx(request):
    return render(request,"bx.html")
