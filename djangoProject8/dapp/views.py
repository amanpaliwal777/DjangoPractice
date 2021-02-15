from django.shortcuts import render

# Create your views here.
def show_details(request,my_id):

    return render(request,'show.html',{'id':my_id})

def home(request):
    return render(request,'home.html')