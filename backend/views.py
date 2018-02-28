from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.serializers import ExpositionSerializer, PictureSerializer
from backend.models import *
from PIL import Image


@api_view(['GET', 'POST'])
def check(request):
    if request.method == 'GET':
        expositions = Exposition.objects.all()
        serializer = ExpositionSerializer(expositions, many=True)
        return Response(serializer.data)
    else:
        return Response(data={"status": "ok"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def return_picture(request):
    if request.method == 'GET':
        pic = Picture.objects.get(id=request.GET.get('pk', 1))
        r = Image.open(pic.image.path)
        response = HttpResponse(content_type="image/jpeg")
        r.save(response, "JPEG")
        return response


@api_view(['GET'])
def return_expo(request):
    if request.method == 'GET':
        pics = Picture.objects.filter(exposition=request.GET.get('num', 1))
        serializer = PictureSerializer(pics, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)
