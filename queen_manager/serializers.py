from rest_framework import serializers

from .models import Queen


class QueenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Queen
        fields = '__all__'
