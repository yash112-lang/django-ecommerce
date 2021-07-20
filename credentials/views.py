from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib import messages
from django.contrib.auth import login as auth_login

# Create your views here.

def signup(request):
    # return HttpResponse("This is user signup page.")
    return render(request, 'user_signup.html')

def login(request):
    # return HttpResponse("This is user login page.")
    return render(request, 'user_login.html')

def seller_signup(request):
    return HttpResponse("This is seller signup page.")

def seller_login(request):
    return HttpResponse("This is seller login page.")

def create_user_account(request):
    if request.method == "POST":
        email = request.POST.get('username')
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword and len(password) <= 0:
            return redirect('/credentials/signup/')
        else:
            # request.SESSION['username'] = username
            myUser = User.objects.create_user(username, email, password, is_staff=False)
            myUser.save()
            return HttpResponse("Account created successfully. You are redirected to home page.")

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(password) <= 0:
            return redirect('/credentials/login')
        else:
            user = authenticate(request, username=email, password=password)
            print(email, password)
            if user is not None:
                if(user.is_staff):
                    auth_login(request, user)
                    # return HttpResponse("You are login as seller account")
                    return redirect('/seller/index')
                else:
                    auth_login(request, user)
                    return redirect('/buyer/index')
            else:
                return redirect('/credentials/login')

def seller_signup(request):
    return render(request, 'seller_signup.html')

def create_seller_account(request):
    if request.method == "POST":
        email = request.POST.get('username')
        username = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password != cpassword and len(password) <= 0:
            return redirect('/credentials/signup/')
        else:
            myUser = User.objects.create_user(username=username, email=email, password=password, is_staff=True)
            myUser.save()
            return HttpResponse("You are created your account as seller account")
    return redirect('credentials/login')

def logout_user(request):
    logout(request)
    return redirect('/credentials/login')
