from django.shortcuts import render, redirect
import pyrebase
from django.http import HttpResponse
from django.contrib import auth

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

config = {
    "apiKey": "AIzaSyAh4r10gdes4ePXAOrzL64XUKm5FVfczXU",
    "authDomain": "korsega-b590c.firebaseapp.com",
    "projectId": "korsega-b590c",
    "storageBucket": "korsega-b590c.appspot.com",
    "messagingSenderId": "58583786390",
    "appId": "1:58583786390:web:4745cc1e647ca8ea2273b7",
    "measurementId": "G-VFN36SXGM2",
    "databaseURL": "https://korsega-b590c-default-rtdb.firebaseio.com",
}

firebase = pyrebase.initialize_app(config)
auth_ = firebase.auth()
db = firebase.database()

def PostSignin(request):
    email = request.POST.get('email')
    Password = request.POST.get('Password')

    user = auth_.sign_in_with_email_and_password(email, Password)
    print(user)

    # user_django = authenticate(email, Password)
    # print(user_django)
    
    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    try:
        user = auth_.sign_in_with_email_and_password(email, Password)
        return redirect("/topic")

    except:
        message = "invalid cerediantials"
        return render(request, "signin.html", {"msg": message})

    
def PostSignup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = auth_.create_user_with_email_and_password(email, password)

    uid = user['localId']
    data = {
        'name':username,
        'status': 1
    }
    db.child('users').child(uid).child("details").set(data)

    print(user)

    session_id = user['idToken']
    request.session['uid'] = str(session_id)

    try:
        user = auth_.sign_in_with_email_and_password(email, password)
        return redirect("/topic")
    except:
        message = "invalid cerediantials"
        return render(request, "signup.html", {"msg": message})

def logout(request):
    try:
        request.session['uid']
    except:
        pass
    return render(request,'home.html')


def forgot_password(request):
    email = request.POST.get('email')
    auth_.send_password_reset_email(email)

    try:
        message = "Please check your email"
        return render(request,'home.html',{"msg":message})
        
    except:
        message = "Some thing went wrong Please try again later"
        return render(request,'page.html',{"msg":message})

def youtube(request):
    return None