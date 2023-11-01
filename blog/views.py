from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse, JsonResponse
from .models import Project
from .forms import createForm
# Create your views here.

def index(request):
    return render(request,'index.html')


# def about(request):
#     return render(request, 'about.html')
    

def hello(request, username):
    return HttpResponse('<h2>Probando mi app Blog. %s </h2>' % username)



def projects(request):
    project = Project.objects.all()
    # Project.objects.create(name=request.Post["name"])
    return render(request, 'projects.html',{'projects':project})
    # redirect('')

def vista(request):
    view_register = Project.objects.all()
    return render(request,'base2.html',{'vista':view_register})

# def vista(request):
#     view_register = Project.objects.all()
#     return render(request,'about.html',{'vista':view_register})   

                       

def contact_us(request):
    create_contact = createForm()
    return render(request,"contact_us.html",{'create_contact':create_contact})

def create_contact(request):
    if request.method == "POST":
         formulario = createForm(request.POST)        
         formulario.save()
         return redirect('index')
     



    # return render(request,"contact_us.html")
    
     

   

