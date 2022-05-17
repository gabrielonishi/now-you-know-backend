from rest_framework import serializers
from .models import Artist, UserTry

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'average_rating']

class UserTrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTry
        fields = ['id', 'score', 'artist']