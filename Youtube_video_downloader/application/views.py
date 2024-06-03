from django.shortcuts import render,redirect
from .models import *
from pytube import *
from pytube.exceptions import VideoUnavailable, PytubeError
import http.client
import socket

# Create your views here.

def youtube(request):
    history=[]
    if request.method=="POST":
        link=request.POST.get('link')
        video=YouTube(link) #provides various methods and attribute to intract with that video,it allowa you to retrive information about that video
        stream=video.streams.get_lowest_resolution() #options for downloding 1.get_highest_resolution() 2. video.streams.filter(res="720p").first()
        stream.download()
        title=video.title
        obj=video_historey(link=link,title=title)
        obj.save()
        return redirect('youtube')
    history = video_historey.objects.all()
    return render(request, 'link.html',context={'history': history})

def audio(request):
    if request.method == "POST":
        link = request.POST.get('link')
        try:
            audio = YouTube(link)
            stream = audio.streams.filter(only_audio=True).first()
            if stream:
                try:
                    stream.download()
                    title=audio.title
                    obj=audio_historey(link=link,title=title)
                    obj.save()
                    message = "Audio downloaded successfully."
                except (http.client.IncompleteRead, socket.error) as e:
                    message = f"Network error occurred: {str(e)}"
            else:
                message = "No audio stream found."
        except VideoUnavailable:
            message = "Video unavailable. Please check the link."
        history = audio_historey.objects.all()
        return render(request, 'audio.html', {'history':history,'message': message})
    history = audio_historey.objects.all()
    return render(request, 'audio.html',context={'history':history})


def clear_video_historey(request):
    obj=video_historey.objects.all()
    obj.delete()
    return render(request,'link.html')


def clear_audio_historey(request):
    obj=audio_historey.objects.all()
    obj.delete()
    return render(request,'audio.html')



