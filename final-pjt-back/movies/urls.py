from django.urls import path
from . import views

urlpatterns = [
    # 전체 영화 목록
    path('list/', views.movie_list),
    # seeding
    path('seeding/', views.seeding),
    # 인기 top 10 영화
    path('popularity/', views.movie_popularity),
    # 장르별 random 영화 10개
    path('genre/<int:genre_id>/', views.genre),
    # tag별 영화
    path('tags/<int:movie_id/', views.tags),
]
