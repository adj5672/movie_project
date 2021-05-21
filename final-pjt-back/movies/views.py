from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializers
from community.serializers import ReviewListSerializer
import requests
from .models import Movie
import random

API_KEY = '28d059b233996387ca26ecda76d580cb'

@api_view(['GET'])
def seeding(request):
    for pageNum in range(1, 50): 
        URL = f'https://api.themoviedb.org/3/movie/now_playing?api_key={API_KEY}&language=ko-KR&page={pageNum}'
        res = requests.get(URL).json()
        for movie_info in res['results']:
            if not Movie.objects.filter(id=movie_info['id']).exists():
                serializer = MovieSerializers(data=movie_info)
                if serializer.is_valid(raise_exception=True):
                    movie = serializer.save(id=movie_info['id'])
                    for genre in movie_info['genre_ids']:
                        movie.genres.add(genre)
    return Response('성공적으로 가져왔습니다.')

@api_view(['GET', ])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def movie_popularity(request):
    movies = Movie.objects.all().order_by('-popularity')[:10]
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def genre(request, genre_id):
    movies = Movie.objects.filter(genres=genre_id).order_by('?')[:10]
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

# 태그에 포함된 영화 10개 정보
@api_view(['GET', ])
def tags(request, movie_id):
    movies = Movie.objects.all()
    reviews = movies.review_set.all()
    
    tags = {
        '기쁨': 0,
        '슬픔': 0,
        '짜증': 0,
        '심심': 0,
        '사랑': 0,
    }
    for review in reviews:
        for tag in tags:
            if tag == review.tags:
                tags[tag] += 1
    
    MAX = 0
    for tag in tags:
        if tags[tag] > MAX:
            max_tag = tag
            MAX = tags[tag]
    
    print(tags)

    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
    
    


