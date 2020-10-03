
from django.shortcuts import render, HttpResponse, redirect
import joblib
import numpy as np
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#Home Page or index page
def index(request):
    return render(request, 'index.html')

#About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    if request.method=="POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        messages.success(request, "Thanks For Contacting Us We Will Manage Your Feedback  ")
    return render(request, 'contact.html')
#Result Page
def result(request):
    cls = joblib.load("final_model.sav")
    
    
    Experience=request.POST["Experience"]
    if Experience.isnumeric():

        Experience=np.reshape(Experience,(-1, 1))
        Experience=Experience.astype('float64')
           #    Experience=np.array([[0]])
        print(Experience)
        result= cls.predict(Experience)
        result=result.item()
        result=round(result, 2)
        return render(request, 'result.html', {'result':result})

    else:
        messages.error(request, 'Please Provide Your Experience in Number ')
        return redirect('mainApp')

#Signup page
def handleSignup(request):
    if request.method=="POST":
        # Get the post parameter
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # Chack for error input
        if not username.isalnum():
            messages.error(request, 'username must contain only letters and numbers ')
            return redirect('mainApp')

        if pass1 != pass2:
            messages.error(request, 'Password does not match')
            return redirect('mainApp')


        #Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'Congrates You have successfully created an account')

        return redirect('mainApp')

    else:
        return HttpResponse('404 - Not Found')
#Login Page
def handleLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user= authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('mainApp')
        else:
            messages.error(request, 'You Have Entered Invalid Credential, Please try again')
            return redirect('mainApp')
    return HttpResponse('404 - Not Found')
#Logout
def handleLogout(request):
    
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('mainApp')
