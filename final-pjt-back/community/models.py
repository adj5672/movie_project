from django.db import models
from django.conf import settings
from movies.models import Movie

class Review(models.Model):
    TAGS_CHOICES = [
        ('기쁨', '기쁨'),
        ('슬픔', '슬픔'),
        ('짜증', '짜증'),
        ('심심', '심심'),
        ('사랑', '사랑'),
    ]
    # 기분을 나타내는 tag
    tags = models.CharField(
        max_length = 2,
        choices = TAGS_CHOICES,
        default = '기쁨',
    )
    title = models.CharField(max_length=100)
    # 0점 ~ 5점 평점
    rank = models.IntegerField(
        choices = [
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ],
        default = 0
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
