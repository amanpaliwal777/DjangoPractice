from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registrations, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_change_pass, name='changepass'),
    path('setpass/', views.user_setpass, name='setpass'),
]
