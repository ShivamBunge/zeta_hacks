from profession.models import portfolio
from profession.models import Profession
from django.contrib.messages.api import error
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import Profile
# Create your views here.


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        elif user is super:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request,"login.html")
def register(request):

    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                return redirect("login")    
        else:
            messages.info(request,"Password not matching.")
            return redirect("register")
    else:
        return render(request,'register.html')

def index(request):
    return render(request,'index.html')

def start(request):
    if (request.user.is_authenticated):
        profs = Profession.objects.all()
        return render(request,"pg0.html",{'profs':profs})
    else:
        return redirect("login")

def logout(request):
    auth.logout(request)
    return redirect("/")

def prof_ch(request):
    player = Profile.objects.get(user__id=request.user.id)
    if request.method=="POST":
        choice=request.POST['select']
        player.current_job=choice
        player.save()
        jobs=portfolio.objects.filter(prtf_name=choice)
        # print(player.current_job)
        if choice=="Doctor":
            return render(request,"pg1-dr.html",{"jobs":jobs})
        elif choice=="Businessman":
            return render(request,"pg1-busi.html")
        elif choice=="Engineer":
            return render(request,"pg1-eng.html")
        elif choice=="Police":
            return render(request,"pg1-pol.html",{"jobs":jobs})
    else:
        redirect("start")

def update_val(request):
    # job=Profession.objects.filter()
    print(job)
    if request.method=="POST":
        return redirect("/")