from rest_framework import serializers, fields

from backend.models import Exposition, Picture


class ExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposition
        fields = ('name', 'description', 'expiration_date')


class PictureSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Picture
        fields = ('id', 'image_url')

    def get_image_url(self, picture):
        request = self.context.get('request')
        image_url = picture.image.url
        return request.build_absolute_uri(image_url)
