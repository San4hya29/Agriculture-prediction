from django.urls import path,include
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.register, name='register'),
    path('login/', views.login_user , name='login'), 
    path('welcome/', views.welcome, name='welcome'),
    path('crop/', views.crop, name='Crop'),
    path('crop/result/', views.result, name='Result'),
    path('fertilizer/', views.ferti, name='fertilizer'),
    path('fertilizer/predict/', views.predict, name='result'),
    path('admin/new/admindashboard/', views.admindashboard, name='admindashboard'),
    path('weather/', views.weather, name='Weather'),
    path('feedbackform/feedback', views.feedback, name='feedback'),
    path('feedbackform/', views.feedbackform, name='feedbackform'),
    path('admin/', admin.site.urls, name='admin'),
]