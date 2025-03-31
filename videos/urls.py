from django.urls import path
from .views import VideoUploadView,VideoListView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='upload-video'),
     path('list/', VideoListView.as_view(), name='list-videos'),
]


