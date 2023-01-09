from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from student.models import Student


class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields=['username','email','password1','password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['User']
        widgets={
            'profileimage': forms.FileInput(attrs={'class':"form-control"}),
            'FirstName': forms.TextInput(attrs={'class':"form-control"}),
            'LastName': forms.TextInput(attrs={'class':"form-control"}),
            'Gender': forms.Select(attrs={'class':"form-select"}),
            'department': forms.Select(attrs={'class':"form-select"}),
            'Level': forms.Select(attrs={'class':"form-select"}),
        }
