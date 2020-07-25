from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, "generator/home.html")

# def style(request):
#     return render(request, "generator/style.css")

def password(request):
    thepassword=""
    chars=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get("length", 10))
    if request.GET.get("Uppercase"):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("Special"):
        chars.extend(list("!@#$%^&*()"))
    if request.GET.get("Numbers"):
        chars.extend(list("0123456789"))
    for x in range(length):
        thepassword +=random.choice(chars)
    return render(request, "generator/password.html", { "password":thepassword})

def about(request):
    return render(request, "generator/about.html")