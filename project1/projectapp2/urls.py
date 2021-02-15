from django.urls import path
from . import views
urlpatterns = [
    path('django/',views.feedj),
    path('python/',views.feepy),

]
