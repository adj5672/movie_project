from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        

class MovieSerializers(serializers.ModelSerializer):

    genres = GenreSerializers(many=True, read_only=True)
    
    class Meta:
        model = Movie
        exclude = ('like_users', )