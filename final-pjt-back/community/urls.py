from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>/', views.reviews),
    path('<int:movie_id>/like/', views.like_movie),
    path('<int:movie_id>/review/<int:review_id>/', views.review),
    path('<int:movie_id>/review/<int:review_id>/comment/<int:comment_id>/', views.comment),
]