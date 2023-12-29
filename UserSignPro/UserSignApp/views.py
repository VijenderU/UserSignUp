from django.shortcuts import render, HttpResponse, redirect
from .models import UserReg

# Create your views here.
def user_signup(request):
    if request.method == "POST":
        uname = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confpassword = request.POST["conpassword"]
        if password != confpassword:
            return HttpResponse("Password doesn't match")
        else:
            user = UserReg(user_name=uname, user_email=email, user_password=password, user_con_password=confpassword)
            user.save()
            return redirect(user_login)
    return render(request, "registration.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user_details = UserReg.objects.all()
        user = None
        for usr in user_details:
            if (usr.user_name,usr.user_password) == (username,password):
                user = usr.user_name
                request.method = ""
                break
        if user is not None:
            return redirect(home_page)
        else:
            return HttpResponse("Invaild Credintials.")
    return render(request,"login.html")

def home_page(request):
    if request.method == "POST":
        
        return redirect(user_login)
    return render(request,"home.html")

# def user_logout(request):
#     return redirect(user_login)
