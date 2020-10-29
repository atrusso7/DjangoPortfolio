from django.db import models
from datetime import date

class Job(models.Model):
    image = models.ImageField(upload_to='static/images/')
    job_title = models.CharField(max_length=100, default='title')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    current_job = models.BooleanField(default=False)
    company_name = models.CharField(max_length=100, default='company')
    summary = models.TextField(default='summary')
    def __str__(self):
        return '{self.job_title}, {self.company_name}'.format(self=self)

class Highlights(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    highlights = models.CharField(max_length=300, default='highlight')
    def __str__(self):
        return self.highlights

class Bio(models.Model):
    bio = models.TextField(default="bio")
    def __str__(self):
        return self.bio

class BioPic(models.Model):
    image = models.ImageField(upload_to='static/images/')

class Certifications(models.Model):
    cert_title = models.CharField(max_length=200)
    cert_company = models.CharField(max_length=200)
    cert_badge = models.TextField(default='')
    def __str__(self):
        return self.cert_title

class BackgroundImage(models.Model):
    image = models.ImageField(upload_to='static/images')

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    def __str__(self):
        return self.school
    


    
    

