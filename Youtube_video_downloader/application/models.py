from django.db import models

# Create your models here.

class video_historey(models.Model):
    link=models.CharField(max_length=50)
    title=models.CharField(max_length=5000,default="string")


    def __str__(self):
        return self.link
    

class audio_historey(models.Model):
    link=models.CharField(max_length=50)
    title=models.CharField(max_length=5000,default="string")


    def __str__(self):
        return self.link
