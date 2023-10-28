from rest_framework import serializers
from .models import *


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializers(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song=serializers.HyperlinkedRelatedField(view_name='song-detail',many=True,read_only=True)
    # song=serializers.SlugRelatedField(slug_field='title',many=True,read_only=True)
    # song=serializers.HyperlinkedIdentityField(view_name='song-detail')
    song=SongSerializers(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gander','song']
