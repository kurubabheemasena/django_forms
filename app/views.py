from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def DJ_forms(request):
    fo=form()
    d={'forms':fo}
    if request.method=='POST':
        fd=form(request.POST)
        if fd.is_valid():
            n=fd.cleaned_data['name']
            a=fd.cleaned_data['age']
            m=fd.cleaned_data['email']
            p=fd.cleaned_data['passwords']
            ad=fd.cleaned_data['address']
            g=fd.cleaned_data['gender']
            c=fd.cleaned_data['course']
            d1={'n':n,'a':a,'m':m,'p':p,'ad':ad,'g':g,'c':c}
            return render(request,'form_data.html',d1)
        
    return render(request,'django_forms.html',d)




