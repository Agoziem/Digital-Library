from django.urls import path
from .views import *

app_name = 'Accounts'
urlpatterns = [
    path('login/', loginPage, name='login'),
    path('signup/', registerPage, name='sign-up'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', Profile_view, name='profile'),
    path('profile/<int:id>', Profile_update_view, name='profileupdate'),
    path('forget_password/', resetpassword_view, name='reset'),
]