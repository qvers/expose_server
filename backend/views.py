from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.serializers import ExpositionSerializer
from backend.models import Exposition
from PIL import Image

# Create your views here.
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
    red = Image.new('RGBA', (10, 10), (255, 0, 0, 0))
    response = HttpResponse(content_type="image/jpeg")
    red.save(response, "JPEG")
    return response
