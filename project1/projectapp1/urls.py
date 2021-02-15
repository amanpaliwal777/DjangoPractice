from django.urls import path
from . import views

urlpatterns = [
    path('django/',views.learndj),
    path('python/',views.learnpy),
]

