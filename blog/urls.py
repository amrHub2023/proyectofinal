from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('base2/', views.vista, name="base2"),   
    path('projects/', views.projects, name="projects"),        
    path('contact_us/', views.contact_us, name="contact_us"),
    path('contact_us/create_contact/', views.create_contact, name="create_contact"),
    # path('contact_us/', views.contactUs, name="contact_us"),
     ]
  
 # path('tarea/', views.tarea, name="tarea"),  