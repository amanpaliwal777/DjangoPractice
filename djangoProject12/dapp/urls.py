from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_user, name='logout'),
]
