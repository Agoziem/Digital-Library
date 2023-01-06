from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Resources.models import *
from student.models import *


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            email =request.POST.get('email')
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                print(user)
                messages.success(request, 'Account was created for ' + user)
                return render(request,'Profile.html') #Redirect Calls on the Url function directory
                
    context={
        "form":form
    }
    return render(request,'register.html',context)

def Profile_view(request):
    user=request.user
    Departments=department.objects.all()
    if request.method == 'POST':
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        dept = request.POST.get('dept')
        Dept=department.objects.get(id=dept)
        Level = request.POST.get('Level')
        Gender = request.POST.get('Gender')
        file =request.FILES['file']
        student=Student.objects.create(User=user,FirstName=Firstname,LastName=Lastname,department=Dept,Level=Level,Gender=Gender,profileimage=file)
        student.save()
        messages.success(request, 'your Profile was created Successfully')
        return redirect('Accounts:login')
        
    context={
       "Departments":Departments, 
    }
    return render(request,"profile.html",context)

def Profile_update_view(request,id):
    student=Student.objects.get(id=id)
    user=request.user
    Departments=department.objects.all()
    if request.method == 'POST':
        Firstname = request.POST.get('Firstname')
        Lastname = request.POST.get('Lastname')
        dept = request.POST.get('dept')
        Dept=department.objects.get(id=dept)
        Level = request.POST.get('Level')
        Gender = request.POST.get('Gender')
        file =request.FILES['file']

        student.FirstName=Firstname
        student.LastName=Lastname
        student.Gender=Gender
        student.department=Dept
        student.Level=Level
        student.profileimage=file
        student.save()
        messages.success(request, 'your Profile was update Successfully')
        return redirect('Accounts:login')
        
    context={
       "Departments":Departments,
       "student":student,
       
    }
    return render(request,"profile_update.html",context)

def logoutUser(request):
	logout(request)
	return redirect('Accounts:login')

def resetpassword_view(request):
    context = {
    }
    return render(request, 'forgot-password.html', context)