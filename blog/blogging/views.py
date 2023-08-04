from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from blogging.models import BlogData

def home(request):
    logintype=request.POST.get('logintype')
    global val
    def val():
        return logintype
    if logintype:
        return redirect('login')

    return render(request,'home.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(request,username=username,password=pass1)
        print(username,pass1)
        if user is not None:
            login(request,user)
            return redirect('blogForm')
        else:
            return HttpResponse("incorrect details")
            
        
    return render(request,'login.html',{'logintype':val()})

def signup(request):
 
    if request.method=='POST':
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2') 
        if pass1==pass2:
            if User.objects.filter(username=username).exists() :
                return HttpResponse("user already exists...")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("email already exists...")
            else:
                my_user=User.objects.create_user(username,email,pass1)
                my_user.first_name=fname
                my_user.last_name=lname
                my_user.save()
                print("yes")
                return redirect('login')
                
        else:
            return HttpResponse("Your password and confirm password mismatches")
    return render(request,'signUp.html')

@login_required(login_url='login')
def blogForm(request):
    blogs=BlogData.objects.all()
    logintype=False
    if val()=="Lecturer":
        logintype=True
    return render(request,'blogForm.html',{'blogs':blogs,'logintype':logintype})

def create(request):
    if request.method=="POST":
        blogtitle=request.POST.get('blogtitle')
        title=request.POST.get('title')
        image=request.POST.get('image')
        desc=request.POST.get('desc')
        files=request.POST.get('files')
        blogs=BlogData(blogtitle=blogtitle,title=title,image=image,desc=desc,files=files)
        blogs.save()
        print(blogtitle,title)
        return redirect('blogForm')
    return render(request,'create.html')