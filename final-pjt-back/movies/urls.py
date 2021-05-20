from django.urls import path
from . import views

urlpatterns = [
    path('', views.seeding),
    path('list/', views.movie_list),
]

