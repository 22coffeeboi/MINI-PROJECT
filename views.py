import datetime
import io
import json
import xlwt
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.urls import reverse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas

from .forms import NameForm, RegForm, admins

import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Create your views here.


config = {
    "apiKey": "AIzaSyAPppt439TK0Xra0JrUXzPG5Y_nzwjw9VM",
    "authDomain": "ven-u-book.firebaseapp.com",
    "projectId": "ven-u-book",
    "storageBucket": "ven-u-book.appspot.com",
    "messagingSenderId": "723635461555",
    "appId": "1:723635461555:web:e02e9de3466872a4867fc6",
    "measurementId": "G-JC4YK9DC8J",
    "databaseURL": "https://ven-u-book-default-rtdb.firebaseio.com/"
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
flag = None
idu = None


def reads(request, checkuser1, admin1):  # decision if its admin or user
    request.session['_old_post'] = request.POST

    print(request.session.get('_old_post'))
    if request.method != 'POST':
        return HttpResponse("invalid attempt1")
    elif admin1 == 1:
        return redirect("sup", check=checkuser1)
    else:
        return redirect("user", check=checkuser1)


def say_hello(request):  # login page loading
    form = NameForm()
    count = database.child('room').shallow().get().val()
    currcount = 0
    for i in count:
        if database.child('room').child(i).child('bookedby').get().val() == "":
            currcount += 1

    length1 = len(count)
    if request.method == 'POST':
        return get_name(request)
    elif request.method == 'GET':

        return render(request, 'index.html', {'form': form,
                                              'count': length1,
                                              'curr': currcount})
    else:

        return render(request, 'index.html', {'form': form,
                                              'count': length1,
                                              'curr': currcount})


def book(request):  # book by user
    print(request.GET)
    if request.method == "GET":
        name = request.GET.get('name')
        room = request.GET.get('room')
        person = database.child('user').shallow().get().val()
        date = datetime.date
        print(date)
        for i in person:
            if database.child('user').child(i).child('name').get().val() == name:
                database.child('user').child(i).update({'req': 1})
                database.child('user').child(i).update({'rm': room})
                database.child('user').child(i).update({'accept': 0})
                database.child('user').child(i).update({'reject': 0})

    return JsonResponse({'res': "request sent"})


@csrf_exempt
def reject(request):  # reject by admin
    print(request.GET)
    if request.method == "GET":
        name = request.GET.get('name')
        print(name)
        person = database.child('user').shallow().get().val()
        for i in person:
            if database.child('user').child(i).child('name').get().val() == name:
                database.child('user').child(i).update({'reject': 1})
                database.child('user').child(i).update({'accept': 0})
                database.child('user').child(i).update({'req': 0})
                database.child('user').child(i).update({'rm': ""})
                break
        return JsonResponse({'res': "REJECTED"})


@csrf_exempt
def accept(request):  # accept by admin
    print(request.GET)
    if request.method == "GET":
        name = request.GET.get('name')
        print(name)
        person = database.child('user').shallow().get().val()
        for i in person:
            if database.child('user').child(i).child('name').get().val() == name:
                database.child('user').child(i).update({'accept': 1})
                database.child('user').child(i).update({'reject': 0})
                database.child('user').child(i).update({'req': 0})
                room1 = database.child('user').child(i).child("rm").get().val()
                if database.child('room').child(room1).child('bookedby').get().val() != "":
                    return reject(request)
                else:
                    current_datetime = datetime.datetime.now()
                    json_str = json.dumps({'created_at': current_datetime}, default=str)
                    database.child("room").child(room1).update({'datime': json_str})
                    database.child("room").child(room1).update({'bookedby': name})
                    break

        return JsonResponse({'res': "ACCEPTED"})


def rq1(request):  # admin side view req from user
    if request.method == "GET":
        list1 = []
        req = int()
        person = database.child('user').shallow().get().val()

        for i in person:
            req = database.child('user').child(i).child('req').get().val()
            print("inside req")

            if req > 0:
                user = database.child('user').child(i).child('name').get().val()
                rm = database.child('user').child(i).child('rm').get().val()

                rqdict = {"name": user,
                          "rm": rm}
                list1.append(rqdict)

    return JsonResponse({"rqs": list1})


"""def export1(request):
    xval = 300
    yval = 700
    room1 = database.child('room').shallow().get().val()

    for key in room1:
        if database.child('room').child(key).child('bookedby').get().val() != "":
            nameofbooker1 = database.child('room').child(key).child('bookedby').get().val()
            line = nameofbooker1 +"----------"+ key
            p = canvas.Canvas()

            p.drawCentredString(xval, yval, nameofbooker1 + "------" + key)
            p.showPage()
            p.save()

    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')"""


def export1(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="booking.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    row_num = 0
    ws = wb.add_sheet('booking data')  # this will make a sheet named Users Data
    columns = ['Time', 'Roomno', 'User']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])
    rooms = database.child('room').shallow().get().val()
    for i in rooms:

        if database.child('room').child(i).child('bookedby').get().val() != "":
            row_num += 1
            tim = database.child('room').child(i).child('datime').get().val()
            us = database.child('room').child(i).child('bookedby').get().val()
            ws.write(row_num, 0, tim)
            ws.write(row_num, 1, i)
            ws.write(row_num, 2, us)
    wb.save(response)
    return response


def room(request):  # returning list of rooms to user side
    rooms = database.child('room').shallow().get().val()
    listroom = []
    for i in rooms:
        res = database.child('room').child(i).child('res').get().val()
        if database.child('room').child(i).child('bookedby').get().val() == "":
            rodict = {"name": i,
                      "resource": res,
                      }
            listroom.append(rodict)
    return JsonResponse({"rooms": listroom})


def uuser(request, check):  # user login
    pending = database.child('user').child(idu).child('req').get().val()
    acc1 = database.child('user').child(idu).child('accept').get().val()
    rej1 = database.child('user').child(idu).child('reject').get().val()
    if pending is None:
        pending = "0"
    if acc1 == 1:
        desc = "ACCEPTED"
    elif rej1 == 1:
        desc = "REJECTED"
    else:
        desc = ""
    return render(request, 'user.html', {"name": check, "pend": pending, "decs": desc})


def insro(request):  # admin insertion room
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = admins(request.POST)
        # check whether it's valid:
        if form.is_valid():
            an = form.cleaned_data["adminname"]
            rn = form.cleaned_data["roomnum"]
            rs = form.cleaned_data["reso"]
            data = {

                "admin": an,
                "res": rs,
                "bookedby": "",
            }
            database.child("room").child(rn).set(data)
            messages.success(request, 'Submited Successfully')


def superad(request, check):  # admin login
    old_post = request.session.get('_old_post')
    if request.method == 'POST':
        insro(request)
    if '_old_post' not in request.session:
        return HttpResponse("invalid attempt2")
    if old_post['name'] == check:
        # del request.session['_old_post']
        form = admins(initial={'adminname': check})
        return render(request, 'admin.html', {"name": check, "form": form})
    else:
        return HttpResponse("invalid attempt3")


def reg(request):  # registeration loading
    if request.method == 'POST':
        return insert(request)

    form = RegForm()
    return render(request, 'reg.html', {'form': form})


def get_arecord(request):  # admin views booked rooms
    room1 = database.child('room').shallow().get().val()

    list3 = []
    for key in room1:
        if database.child('room').child(key).child('bookedby').get().val() != "":
            nameofbooker1 = database.child('room').child(key).child('bookedby').get().val()
            print(nameofbooker1)
            adict = {'name': nameofbooker1,
                     'room': key}
            list3.append(adict)
    return JsonResponse({'areqs': list3})


def get_name(request):  # login
    x = database.child('count').get().val()
    list1 = []
    admin1 = 0
    global idu
    global flag

    checkuser1 = ""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n = form.cleaned_data["name"]
            np = form.cleaned_data["pasn"]
            data = {

                "name": n,
                "pass": np,
            }

            # database.child('user').child(x).set(data)
            # database.child('count').set(x + 1)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            person = database.child('user').shallow().get().val()
            for i in person:
                list1.append(i)
            list1.sort()
            print(list1)
            for i in list1:
                checkuser1 = database.child("user").child(i).child("name").get().val()
                checkpass = database.child("user").child(i).child("pass1").get().val()
                print(checkuser1, checkpass)

                if checkuser1 == n and checkpass == np:
                    flag = "accept"
                    admin1 = database.child('user').child(i).child('admin').get().val()
                    idu = i
                    print(admin1)
                    break

    # if a GET (or any other method) we'll create a blank form
    if flag == "accept":
        print("inside1")
        flag = ""
        print(admin1)
        return reads(request, checkuser1, admin1)
    else:
        print("inside 2")
        form = NameForm()
        flag = "reject"
        return render(request, 'index.html', {'flag': flag, 'form': form})


def insert(request):  # register
    x = database.child('count').get().val()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            n = form.cleaned_data["name"]
            np1 = form.cleaned_data["pasn1"]
            np2 = form.cleaned_data["pasn2"]
            npe = form.cleaned_data["email"]
            from_email = settings.EMAIL_HOST_USER
            print(np1, np2)
            data = {

                "name": n,
                "pass1": np1,

                "email": npe,
                "req": 0,
                "accept": 0,
                "reject": 0,
                "rm": "",
            }
            if np1 == np2:
                print(np1, np2)
                database.child('user').child(x).set(data)

                database.child('count').set(x + 1)

                return HttpResponseRedirect("/home/")
            else:
                er1 = "Password doesnt match"
                # this is a comment about what a good guy allen anand is as a classmate.

                print(er1)
                form = RegForm()
                return render(request, 'reg.html', {'error': er1, 'form': form})
