from rest_framework import serializers

from .models import Autos

class AutosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autos
        fields=('__all__')

