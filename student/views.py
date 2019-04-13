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
import openpyxl
import time
from time import sleep
# from sinchsms import SinchSMS
from twilio.rest import Client


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
                mapdict=['name', 'mentor', 'id','number','father','mother'])
            return redirect('student:home')
    else:
        form = UploadFileForm()
    return render(request,'upload_form.html', {'form': form})


def send(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']

            wb = openpyxl.load_workbook(filehandle)
            worksheet = wb["THEORY"]
            print(worksheet)
            i = 4
            while i < 15:
                temp = str(worksheet[i][0].value)
                i = i + 1
                if temp == "None":
                    break
            j = 4
            t1 = str(worksheet[2][4].value)
            print(t1)
            while j < i - 1:
                enroll = str(worksheet[j][0].value)
                print(enroll)
                std = Student.objects.get(id=enroll)
                number = std.number
                fatherNo = std.father
                motherNo = std.mother
                print(number,fatherNo,motherNo)

                sub1 = str(worksheet[2][2].value)
                sub1Total = str(worksheet[j][2].value)
                sub1Attended = str(worksheet[j][3].value)

                # sub2
                sub2 = str(worksheet[2][5].value)
                sub2Total = str(worksheet[j][5].value)
                sub2Attended = str(worksheet[j][6].value)

                # sub3
                sub3 = str(worksheet[2][8].value)
                sub3Total = str(worksheet[j][8].value)
                sub3Attended = str(worksheet[j][9].value)

                # sub4
                sub4 = str(worksheet[2][11].value)
                sub4Total = str(worksheet[j][11].value)
                sub4Attended = str(worksheet[j][12].value)

                # sub5
                sub5 = str(worksheet[2][14].value)
                sub5Total = str(worksheet[j][14].value)
                sub5Attended = str(worksheet[j][15].value)

                # sub6
                sub6 = str(worksheet[2][17].value)
                sub6Total = str(worksheet[j][17].value)
                sub6Attended = str(worksheet[j][18].value)
                print(str(worksheet[j][1].value), "\n", sub1, sub1Attended, " of ", sub1Total, "\n", sub2, sub2Attended,
                      " of ", sub2Total, "\n", sub3, sub3Attended, " of ", sub3Total, "\n", sub4, sub4Attended, " of ",
                      sub4Total, "\n", sub5, sub5Attended, " of ", sub5Total, "\n", sub6, sub6Attended, " of ",
                      sub6Total, "\n")
                j = j + 1

           # sendSMS()
            return redirect('student:home')
    else:
        form = UploadFileForm()
    return render(request,'send_sms.html', {'form': form})


def sendSMS():
    account_sid = 'AC19b68ab50ce8b6d381aa894b97f00ab1'
    auth_token = '82933ed4e3aa3a72d6b13b2afb0176cf'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Join Earth's mightiest heroes. Like Kevin Bacon.",
            from_='+13342923372',
            to='+917984426396'
            )
    print(message.sid)
