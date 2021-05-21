from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializers
from community.serializers import ReviewListSerializer
import requests
from .models import Movie
from django.db.models import Max, F, Case, When, Count, Q

from movies import serializers

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

@api_view(['GET',])
def tags(request, feeling):
    movies = Movie.objects.annotate(
        # count : 달린 리뷰 갯수
        count = Count("review__tags"),
        count1 = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='기쁨')),
        count2 = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='슬픔')),
        count3 = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='짜증')),
        count4 = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='심심')),
        count5 = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='사랑'))
    ).filter(
        # 리뷰가 최소 1개 이상
        Q(count__gt=0) &
        Q(count1__gte=0) &
        Q(count2__gte=0) &
        Q(count3__gte=0) &
        Q(count4__gte=0) &
        Q(count5__gte=0) 
    )
    serializers = MovieSerializers(movies, many=True)
    return Response(serializers.data)
