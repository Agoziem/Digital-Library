from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
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
                try:
                    student=Student.objects.get(User=request.user)
                    return redirect('home')
                except:
                    Student.objects.create(User=request.user)
                    return redirect("Accounts:profile")

            else:
                messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def registerPage(request):
    Departments=department.objects.all()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                Username = form.cleaned_data.get('username')
                messages.success(request, 'Account have been created for you' + Username)
                return redirect('Accounts:login') #Redirect Calls on the Url function directory            
    context={
        "form":form
    }
    return render(request,'register.html',context)

def Profile_view(request):
    user=request.user.student
    form=ProfileForm(instance=user)
    Departments=department.objects.all()
    context={
       "Departments":Departments,
       "form":form,
    }
    if request.method == 'POST':
        form=ProfileForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            form.save()
        # Firstname = request.POST.get('Firstname')
        # Lastname = request.POST.get('Lastname')
        # dept = request.POST.get('dept')
        # Dept=department.objects.get(id=dept)
        # Level = request.POST.get('Level')
        # Gender = request.POST.get('Gender')
        # file =request.FILES['file']
        # if file == "":
        #     student=Student.objects.create(User=user,FirstName=Firstname,LastName=Lastname,department=Dept,Level=Level,Gender=Gender)
        # else:
        #     student=Student.objects.create(User=user,FirstName=Firstname,LastName=Lastname,department=Dept,Level=Level,Gender=Gender,profileimage=file)
        # student.save()
            messages.success(request, 'your Profile was updated Successfully')
            return redirect('Accounts:login')
        # except:
        #     messages.error(request, 'Check your input and try again')
        #     return render(request,"Profile.html",context)
     
    
    return render(request,"Profile.html",context)

def logoutUser(request):
	logout(request)
	return redirect('Accounts:login')

def resetpassword_view(request):
    context = {
    }
    return render(request, 'forgot-password.html', context)