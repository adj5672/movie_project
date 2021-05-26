from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieSerializers
import requests
from .models import Movie
from django.db.models import Count, Q, Avg
import os

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


API_KEY = os.environ.get("DJANGO_APP_API_KEY")

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

@api_view(['GET', ])
def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    tags = movie.review_set.aggregate(
        기쁨 = Count("tags", filter=Q(tags="기쁨")),
        슬픔 = Count("tags", filter=Q(tags="슬픔")),
        짜증 = Count("tags", filter=Q(tags="짜증")),
        심심 = Count("tags", filter=Q(tags="심심")),
        사랑 = Count("tags", filter=Q(tags="사랑"))
    )
    # 태그 별로 갯수 정렬 (key: 태그 이름, value: 해당 태그 갯수)
    sorted_tags = sorted(tags.items(), key=lambda x: x[1], reverse=True)
    # review_cnt: 리뷰의 총 갯수
    review_cnt = movie.review_set.count()
    # 댓글의 평점 평균
    if review_cnt > 0:
        rank_avg = round(movie.review_set.aggregate(Avg("rank"))["rank__avg"], 1)
    else:
        rank_avg = 0
    data = {
        "most_tag": sorted_tags[0][0],
        "tag_count": sorted_tags[0][1],
        "review_cnt": review_cnt,
        "rank_avg": rank_avg
    }
    return Response(data)

@api_view(['GET',])
def genre(request, genre_id):
    movies = Movie.objects.filter(genres=genre_id).order_by('?')[:10]
    serializer = MovieSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def tags(request, feeling):
    movies = Movie.objects.annotate(
        # review_count : 달린 리뷰 갯수
        review_count = Count("review__tags"),
        happy = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='기쁨')),
        sad = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='슬픔')),
        irritation = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='짜증')),
        boring = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='심심')),
        love = Count("review__tags", filter=Q(review__tags=feeling)) - Count("review__tags", filter=Q(review__tags='사랑'))
    ).filter(
        # 리뷰가 최소 1개 이상
        Q(review_count__gt=0) &
        # 각 감정 tag와 갯수 비교 
        Q(happy__gte=0) & Q(sad__gte=0) & Q(irritation__gte=0) & Q(boring__gte=0) & Q(love__gte=0) 
    )

    serializers = MovieSerializers(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movies(request):
    user = request.user
    like_movies = user.like_movies.all()
    serializer = MovieSerializers(like_movies, many=True)
    return Response(serializer.data)