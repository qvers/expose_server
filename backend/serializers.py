from rest_framework import serializers, fields

from backend.models import Exposition


class ExpositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exposition
        fields = '__all__'