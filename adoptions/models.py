from django.db import models

# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'),('f','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=100,choices=SEX_CHOICES,blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine',blank=True)
class Vaccine(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

 
