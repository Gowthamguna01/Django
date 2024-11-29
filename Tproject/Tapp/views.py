from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gov(request):
    return render(request,"index.html")

def bio(request):
    firstname = request.GET['first_name']
    lastname = request.GET['last_name']
    username = request.GET['user_name']
    password = request.GET['password']
    mobile = request.GET['mobile']
    return render(request,"bio.html",
    {
        'Firstname':firstname,
        'Lastname':lastname,
        'Username':username,
        'Password':password,
        'Mobile':mobile,
    }
    )



