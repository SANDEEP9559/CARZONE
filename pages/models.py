from django.db import models

# Create your models here.

class Team(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=900)
    twitter_link = models.URLField(max_length=900)
    linkedin_link = models.URLField(max_length=900)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
