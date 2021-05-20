from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializers
import requests

@api_view(['GET',])
def seeding(request):
    URL = 'https://api.themoviedb.org/3/movie/now_playing?api_key=28d059b233996387ca26ecda76d580cb&language=ko-KR&page=1'
    res = requests.get(URL).json()
    for movie_info in res['results']:
        serializer = MovieSerializers(data=movie_info)
        if serializer.is_valid(raise_exception=True):
            movie = serializer.save()
            for genre in movie_info['genre_ids']:
                movie.genres.add(genre)
            movie.id = movie_info['id']
            movie.save()
    return Response('성공적으로 db에 저장')

