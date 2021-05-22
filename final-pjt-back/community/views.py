from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Review, Comment
from movies.models import Movie
from .serializers import ReviewSerializer, CommentSerializer, ReviewListSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

@api_view(['GET', 'POST',])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def reviews(request, movie_id):
    # 리뷰 가져오기
    if request.method == "GET":
        reviews = Review.objects.filter(movie_id=movie_id)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    # 리뷰 작성
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=movie_id)
        review = ReviewSerializer(data=request.data)
        if review.is_valid(raise_exception=True):
            review.save(movie=movie, user=request.user)
            return Response(review.data)

@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def review(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)

    # 리뷰 상세페이지
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 리뷰 삭제
    if request.method == 'DELETE':
        review.delete()
        return Response({'pk': f'{review_id}번 리뷰가 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    
    # 리뷰 수정
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 댓글 작성
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data)

@api_view(['PUT', 'DELETE', ])
def comment(request, movie_id, review_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    # 댓글 삭제
    if request.method == 'DELETE':
        comment.delete()
        return Response({'pk': f'{comment_id}번 댓글이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    
    # 댓글 수정
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)