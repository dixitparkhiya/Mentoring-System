from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Student
#for django-excel
from django.shortcuts import render_to_response
from django.http import HttpResponseBadRequest
from django import forms
from django.template import RequestContext
import django_excel as excel
###############################################


def home(request):
    return render(request,'homepage.html',{})


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            filehandle.save_to_database(
                model=Student,
                mapdict=['name', 'mentor', 'id','std_no','father','mother'])
            return redirect('student:home')
    else:
        form = UploadFileForm()
    return render(request,'upload_form.html', {'form': form})
