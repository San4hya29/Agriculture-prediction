from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm, FeedbackForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.forms import UserCreationForm 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
import requests
from bs4 import BeautifulSoup
import warnings
from .models import Feedback


def index(request):
    return render(request,'index.html')

def welcome(request):
    return render(request,'welcome.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User = authenticate(username = username, password = password)
            messages.success(request, 'Registered Successful')
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request,'signin.html',{'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return redirect('index') 
    else:    
        return render(request, 'login.html',{})


def crop(request):
    
    return render(request,'crop.html')

def result(request):
        data = pd.read_csv('D:/Agriprj/Data/crop_recommendation.csv')
        X = data.drop('label', axis=1)
        Y = data['label']
        Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size =.30)
        model = GaussianNB()
        model.fit(Xtrain, Ytrain)
        v1 = float(request.GET['N'])
        v2 = float(request.GET['K'])
        v3 = float(request.GET['P'])
        v4 = float(request.GET['R'])
        v5 = float(request.GET['H'])
        v6 = float(request.GET['T'])
        v7 = float(request.GET['Ph'])
        pred = model.predict(np.array([v1,v2,v3,v4,v5,v6,v7]).reshape(1,-1))
        label = "The crop sutiable for you is :"+ str(pred)
        return render(request,'crop.html',{'result2':label})

def ferti(request):
    return render(request,'fertilizer.html')

def predict(request):
    data = pd.read_csv('D:/Agriprj/Data/Fertilizer Prediction.csv')
    data=data.drop(['Temparature'], axis = 1)
    data=data.drop(['Moisture'], axis = 1)
    data=data.drop(['Soil Type'], axis = 1)
    X = data.drop(['Fertilizer Name'], axis=1)
    Y = data['Fertilizer Name']
    Numerics=LabelEncoder()
    X['Crop_n'] = Numerics.fit_transform(X['Crop Type'])
    X_n = X.drop(['Crop Type'], axis=1)
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(X_n, Y, test_size = 0.2)
    model = GaussianNB()
    model.fit(Xtrain, Ytrain)
    var1 = float(request.GET['N'])
    var2 = float(request.GET['K'])
    var3 = float(request.GET['P'])
    var4 = float(request.GET['R'])
    var5 = Numerics.fit_transform([request.GET['C']])[0]
    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1,-1))
    label = "The suitable fertilizer is: " + str(pred)
    return render(request,'fertilizer.html', {'result': label})


def weather(request):
    # enter city name
    city = "lucknow"

    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]

    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]

    # printing all data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    label = "The weather is :"+ temp + "," + time + "," + sky
    return render(request, 'weather.html', {'label': label})


def admindashboard(request):
    
    return render(request,'admindashboard.html')

def feedbackform(request):
    return render(request,'feedback.html')

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            return redirect('index')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})