from django.shortcuts import render
import pyrebase
from django.http import HttpResponse

config = {
    "apiKey": "AIzaSyAh4r10gdes4ePXAOrzL64XUKm5FVfczXU",

  "authDomain": "korsega-b590c.firebaseapp.com",

  "projectId": "korsega-b590c",

  "storageBucket": "korsega-b590c.appspot.com",

  "messagingSenderId": "58583786390",

  "appId": "1:58583786390:web:4745cc1e647ca8ea2273b7",

  "measurementId": "G-VFN36SXGM2",
  "databaseURL" : ""
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def PostSignin(request):
    email = request.POST.get('email')
    Password = request.POST.get('Password')

    user = auth.sign_in_with_email_and_password(email,Password)
    print(user)

    try:
      user = auth.sign_in_with_email_and_password(email,Password)
      return render(request, "welcome.html",{"e":email})
    except:
      message = "invalid cerediantials"
      return render(request,"signIn.html",{"msg":message})
    
    
        