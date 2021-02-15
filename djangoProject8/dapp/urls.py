from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('<my_id>/',views.show_details,name = 'show'),
]