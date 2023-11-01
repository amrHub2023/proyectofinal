from django import forms
from .models import Project


class createForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['name','email', 'phone' ,'message'] 
