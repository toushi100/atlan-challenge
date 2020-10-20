from django.db import models
from django import forms

class Upload(models.Model):
    # the name of the uploaded CSV file
    ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    file = forms.FileField()

    def __str__(self):
        return self.title

class batata(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class file_content(models.Model):
    seq = models.IntegerField(unique = True, primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    dollar = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    date = forms.DateInput(format = '%Y-%m-%d')
    CSV_ID = models.ForeignKey(Upload, on_delete=models.CASCADE,null=True)