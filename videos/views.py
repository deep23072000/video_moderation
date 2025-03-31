from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer



class VideoUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Video uploaded successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VideoListView(APIView):
    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# import os
# import cv2
# import subprocess
# from django.conf import settings
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Video
# from .serializers import VideoSerializer

# class VideoUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             video = serializer.save()
            
#             # Extract frames
#             frame_count = extract_frames(video.video_file.path)
            
#             # Extract audio
#             audio_path = extract_audio(video.video_file.path)

#             # Update video instance
#             video.frame_count = frame_count
#             video.audio_file = audio_path
#             video.save()

#             return Response({
#                 "message": "Video uploaded and processed successfully!",
#                 "data": serializer.data
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class VideoListView(APIView):
#     def get(self, request, *args, **kwargs):
#         videos = Video.objects.all()
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# # Function to extract frames
# def extract_frames(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frame_count = 0

#     output_dir = os.path.join(settings.MEDIA_ROOT, "frames")
#     os.makedirs(output_dir, exist_ok=True)

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)
#         frame_count += 1

#     cap.release()
#     return frame_count

# # Function to extract audio
# def extract_audio(video_path):
#     audio_output_dir = os.path.join(settings.MEDIA_ROOT, "audio")
#     os.makedirs(audio_output_dir, exist_ok=True)

#     audio_filename = os.path.splitext(os.path.basename(video_path))[0] + ".wav"
#     audio_path = os.path.join(audio_output_dir, audio_filename)

#     command = f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path} -y"
#     subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     return audio_path




