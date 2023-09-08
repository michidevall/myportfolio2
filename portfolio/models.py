from django.db import models

# Create your models here.
class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    description = models.TextField()
    ordinal = models.IntegerField()
    

class Work(models.Model):
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    description = models.TextField()
    oridinal = models.IntegerField()
    
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    url = models.URLField(max_length=200)
    ordinal = models.IntegerField()
        