from django.shortcuts import render
from .models import Video
# Create your views here.

def index(request):
   return render(request,'backend/index.html')
def videoupload(request):
   return render(request,'backend/videoupload.html')
def videoprocess(request):
   #code
   if request.method=="POST":
      videoclass = Video(
         video = request.POST.get("video")
      )
      videoclass.save()
      print("Saved file")
   return render(request,'backend/videoupload.html')
