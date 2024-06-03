from django.urls import path
from .views import *

urlpatterns = [
 path('youtube/',youtube,name='youtube'),
 path('audio/',audio,name="audio"),
 path('clear_video_historey/',clear_video_historey,name="clear_video_historey"),
 path('clear_audio_historey/',clear_audio_historey,name="clear_audio_historey"),
]