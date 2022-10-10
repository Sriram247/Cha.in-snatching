from django.db import models
from django.db.models.signals import post_save
import cv2,os
import zipfile,threading   

# Create your models here.

class Video(models.Model):
   video = models.FileField(upload_to="VideoFootages",max_length=None)
   Photos = models.FileField(upload_to="Photos",blank=True,max_length=None)


def Video_recieved(instance, created, **kwargs):
   if created==True:
      vid = instance.video.url
      zip_file_name = "VideoImages.zip"

      vidcap = cv2.VideoCapture("http://localhost:8000"+vid)
      success,image = vidcap.read()
      count = 0
      print("Working: "+ "http://localhost:8000"+ str(vid))
      
      while success:
         # save frame as JPEG file      
         cv2.imwrite("VideoUploads/frame%d.jpg" % count, image)
         success,image = vidcap.read()
         count += 1   

      
post_save.connect(Video_recieved, sender=Video)
