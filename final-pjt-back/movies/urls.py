from django.urls import path
from . import views

urlpatterns = [
    # seeding
    path('seeding/', views.seeding),
    # 전체 영화 목록
    path('list/', views.movie_list),
    # 인기 top 10 영화
    path('popularity/', views.movie_popularity),
    # User가 좋아요를 누를 영화 목록
    path('my_movies/', views.my_movies),
    # 영화 상세 페이지(최대 태그 및 태그 갯수 반환)
    path('<int:movie_id>/', views.detail),
    # 장르별 random 영화 10개
    path('genre/<int:genre_id>/', views.genre),
    # 기분 Tag
    path('tag/<feeling>/', views.tags),
]
