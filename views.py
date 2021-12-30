from django.shortcuts import render,HttpResponseRedirect
from .forms import crud
from .models import crudinfo
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages


from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from time import time
# from .models import Tshirt,Sizevariant,CartProduct,Product,Cart,Order,Orderitem,Payment,Brand,Occasion,Color,Sleeve,Necktype,Idealfor
from math import floor
import sys
from subprocess import run,PIPE
from django.contrib.auth.decorators import login_required
# from instamojo_wrapper import Instamojo
# from newproject.settings import API_KEY,AUTH_TOKEN
# api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
import speech_recognition as sr

import pyttsx3,webbrowser,os,random,pyautogui,requests
import pywhatkit,sys,time
import datetime
import wikipedia
import bs4
import os

from datetime import date
import subprocess



   
def index(request):
    if request.method =="POST":
        obje =crud(request.POST)
        if obje.is_valid:
            obje.save()
            messages.success(request,"Student Added Sucessfully")
            obje = crud()
    else:
        obje =crud()
    stud = crudinfo.objects.all()
    cnt =crudinfo.objects.count()
    return render(request,"index.html",{"form":obje,"stu":stud ,"count":cnt})




def delete_data(request, id):
    if request.method=="POST":
        obje = crudinfo.objects.get(pk=id)
        obje.delete()
        messages.success(request,"Deleted!!!")
        return HttpResponseRedirect("/")

def update_data(request,id):
    if request.method =="POST":
        pi=crudinfo.objects.get(pk=id)
        fm =crud(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Updated !!!!")
            fm=crud()

    else:
        pi=crudinfo.objects.get(pk=id)
        fm =crud(instance=pi)
    return render(request,"update.html",{"form":fm})


