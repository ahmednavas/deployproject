from django.shortcuts import render
import pyrebase
from django.contrib import messages
# Create your views here.

config={
    "apiKey": "AIzaSyDFd5FOA0iMeF7kSvQabNW-p8NwFsCe5z8",
    "authDomain": "cryptic-tower-392606.firebaseapp.com",
    "databaseURL":"https://cryptic-tower-392606-default-rtdb.europe-west1.firebasedatabase.app/",
    "projectId": "cryptic-tower-392606",
    "storageBucket": "cryptic-tower-392606.appspot.com",
    "messagingSenderId": "406727627213",
    "appId": "1:406727627213:web:bb552a7b8f47465586f484",
    "measurementId": "G-3B6P9JPM9G"
}

firebase=pyrebase.initialize_app(config)
authu=firebase.auth()
database=firebase.database()
def home(request):
    if 'signup' in request.POST:
        EMAIL=request.POST['email']
        PASSWORD=request.POST['password']
        try:
           authu.create_user_with_email_and_password(EMAIL,PASSWORD)
           messages.success(request,'sign up success')
        except:
            messages.info(request,'not sign up success')

        
    
  
    return render(request,'index.html')