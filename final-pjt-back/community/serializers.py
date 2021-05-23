from rest_framework import serializers
from .models import Review, Comment
from accounts.serializers import UserSerializer
from movies.serializers import MovieSerializers

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', )

class ReviewSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.IntegerField(source="comment_set.count", read_only=True)
    movie = MovieSerializers(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    comment_cnt = serializers.IntegerField(source="comment_set.count", read_only=True)
    user = UserSerializer(read_only=True)
    movie = MovieSerializers(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    review = ReviewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'