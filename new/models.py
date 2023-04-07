from django.db import models

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=522)

class dashboard(models.Model):
    link = models.URLField(max_length=500)

