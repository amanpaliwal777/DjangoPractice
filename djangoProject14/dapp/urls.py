from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_signup, name='sign_up'),
    path('login/', views.user_login, name='log_in'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changepass/', views.user_changepass, name='changepass'),
]
