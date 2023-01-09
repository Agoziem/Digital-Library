from django.shortcuts import render,redirect
from .models import *
from student.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='Accounts:login')
def home_view(request):
    # For the user profile
    try:
        profile=Student.objects.get(User=request.user)
        deptpage=False
    # For the Message
        student=request.user.student
        Etextbooks=Textbook.objects.filter(Department=student.department,level=student.Level)[:3]
        Pastquestion=PastQuestion.objects.filter(Department=student.department,level=student.Level)[:3]
        materials=Material.objects.filter(Department=student.department,level=student.Level)[:3]
        messagelist=[]
        for textbook in Etextbooks:
            messagelist.append(f"{textbook.Title} Textbook")

        for question in Pastquestion:
            messagelist.append(f"{question.course} Past Question")
        
        for material in materials:
            messagelist.append(f"{material.Title} Material")

        messagecount=len(messagelist)

        #for the Alert System
        Alerts=NewsAlert.objects.all()[:6]
        Alertcount=Alerts.count()

        departments=department.objects.all()
        Chemical,created=department.objects.get_or_create(Name="Chemical")
        Mechanical,created=department.objects.get_or_create(Name="Mechanical")
        Structural,created=department.objects.get_or_create(Name="Structural")
        Civil,created=department.objects.get_or_create(Name="Civil")
        Electrical,created=department.objects.get_or_create(Name="Electrical")
        Production,created=department.objects.get_or_create(Name="Production")
        Agricultural,created=department.objects.get_or_create(Name="Agricultural")
        Mechatronics,created=department.objects.get_or_create(Name="Mechatronics")
        Marine,created=department.objects.get_or_create(Name="Marine")
        Industrial,created=department.objects.get_or_create(Name="Industrial")
        Petroluem,created=department.objects.get_or_create(Name="Petroluem")
        Computer,created=department.objects.get_or_create(Name="Computer")
        Metallurgical,created=department.objects.get_or_create(Name="Metallurgical")
        context={
        "Chemical":Chemical,
            "Mechanical":Mechanical,
            "Structural":Structural,
            "Civil":Civil,
            "Electrical":Electrical,
            "Production":Production,
            "Agricultural":Agricultural,
            "Mechatronics":Mechatronics,
            "Marine":Marine,
            "Industrial":Industrial,
            "Petroluem":Petroluem,
            "Computer":Computer,
            "Metallurgical":Metallurgical,
            "profile":profile,
            "deptpage":deptpage,

            "messagelist":messagelist,
            "messagescount":messagecount,
            "Alerts":Alerts,
            "Alertscount":Alertcount,

        }
        return render(request,'Home.html',context)
    except:
        Departments=department.objects.all()
        context={
       "Departments":Departments, 
            }
        return redirect('Accounts:profile')

    

@login_required(login_url='Accounts:login')
def department_view(request,id,level):
    profile=Student.objects.get(User=request.user)
    deptpage=True
    student=request.user.student
    Etextbooks=Textbook.objects.filter(Department=student.department,level=student.Level)[:3]
    Pastquestion=PastQuestion.objects.filter(Department=student.department,level=student.Level)[:3]
    materials=Material.objects.filter(Department=student.department,level=student.Level)[:3]
    messagelist=[]
    for textbook in Etextbooks:
        messagelist.append(f"{textbook.Title} Textbook")

    for question in Pastquestion:
        messagelist.append(f"{question.course} Past Question")
    
    for material in materials:
        messagelist.append(f"{material.Title} Material")

    messagecount=len(messagelist)

    #for the Alert System
    Alerts=NewsAlert.objects.all()[:6]
    Alertcount=Alerts.count()

    # General Context 
    Chemical,created=department.objects.get_or_create(Name="Chemical")
    Mechanical,created=department.objects.get_or_create(Name="Mechanical")
    Structural,created=department.objects.get_or_create(Name="Structural")
    Civil,created=department.objects.get_or_create(Name="Civil")
    Electrical,created=department.objects.get_or_create(Name="Electrical")
    Production,created=department.objects.get_or_create(Name="Production")
    Agricultural,created=department.objects.get_or_create(Name="Agricultural")
    Mechatronics,created=department.objects.get_or_create(Name="Mechatronics")
    Marine,created=department.objects.get_or_create(Name="Marine")
    Industrial,created=department.objects.get_or_create(Name="Industrial")
    Petroluem,created=department.objects.get_or_create(Name="Petroluem")
    Computer,created=department.objects.get_or_create(Name="Computer")
    Metallurgical,created=department.objects.get_or_create(Name="Metallurgical")


    # Page Level context
    Department=department.objects.get(id=id)

    # Pagination for the E-textbooks
 
    P=Paginator(Textbook.objects.filter(Department=id,level=level),12)
    page=request.GET.get('page')
    Etextbooks=P.get_page(page)
    nums="a" * Etextbooks.paginator.num_pages


    Pastquestion=PastQuestion.objects.filter(Department=id,level=level)
    materials=Material.objects.filter(Department=id,level=level)
    context={
      "Chemical":Chemical,
        "Mechanical":Mechanical,
        "Structural":Structural,
        "Civil":Civil,
        "Electrical":Electrical,
        "Production":Production,
        "Agricultural":Agricultural,
        "Mechatronics":Mechatronics,
        "Marine":Marine,
        "Industrial":Industrial,
        "Petroluem":Petroluem,
        "Computer":Computer,
        "Metallurgical":Metallurgical,
        "profile":profile,
        "deptpage":deptpage,

        "Department":Department,
        "Etextbooks":Etextbooks,
        "Pastquestion":Pastquestion,
        "materials":materials,
        "level":level,
        "nums":nums,

        "messagelist":messagelist,
        "messagescount":messagecount,
        "Alerts":Alerts,
        "Alertscount":Alertcount,


    }
    return render(request,'department.html',context)
