from django.shortcuts import render
from .models import *
from student.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='Accounts:login')
def home_view(request):
    profile=Student.objects.get(User=request.user)
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
        "profile":profile,
    }
    return render(request,'Home.html',context)

@login_required(login_url='Accounts:login')
def department_view(request,id,level):
    profile=Student.objects.get(User=request.user)
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


    # Page Level context
    Department=department.objects.get(id=id)
    Etextbooks=Textbook.objects.filter(Department=id,level=level)
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
        "profile":profile,

        "Department":Department,
        "Etextbooks":Etextbooks,
        "Pastquestion":Pastquestion,
        "materials":materials,
        "level":level


    }
    return render(request,'department.html',context)
