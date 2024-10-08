from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import *
from .services import *


class VideoViewSet(viewsets.ModelViewSet):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer
  permissions_classes = [permissions.AllowAny]

  @action(detail=False, methods=['POST'], permission_classes=[permissions.AllowAny])
  def download_video(self, request, *args, **kwargs):
    url = request.data['url']
    video, name = download_video(url)
    Video.objects.create(
      url=url
    )
    response = HttpResponse(video, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename="{name}"'
    return response
  
  @action(detail=False, methods=['POST'], permission_classes=[permissions.AllowAny])
  def convert_video_to_mp4(self, request, *args, **kwargs):
    video = request.FILES['video']
    if video.content_type == 'video/mp4':
      return Response(
        'Estás enviando un video en mp4, envía otro',
        status=400
      )
    video, name = convert_video(video)
    response = HttpResponse(video, content_type='video/mp4')
    response['Content-Disposition'] = f'attachment; filename="{name}"'
    return response
