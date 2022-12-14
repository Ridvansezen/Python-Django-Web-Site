from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.

@csrf_exempt
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username )
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarıyla kayıt oldunuz...")
        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
            "form" : form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password") 
        user = authenticate(username = username,password = password)  
        if user is None:
            messages.info(request,"Kullanıcı adı veya Parola hatalı !")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla giriş yapıldı...")
        login(request,user)
        return redirect("index")

    return render(request,"login.html",context)    

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yapıldı...")
    return redirect("index")