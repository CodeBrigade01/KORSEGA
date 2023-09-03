from django.shortcuts import render
# import pyrebase
# from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def Signin(request):
    return render(request,"signin.html")

def Signup(request):
    return render(request,"signup.html")

def forgot_passsword(request):
    return render(request,"forgotpassword.html")

