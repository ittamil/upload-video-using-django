from django.shortcuts import render
from app.models import VideoUploader
# Create your views here.

def index(request):
    videos = VideoUploader.objects
    context = {
        'videos' :videos
    }
    return render(request,'index.html',context)