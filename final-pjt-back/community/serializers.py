from rest_framework import serializers
from .models import Review, Comment
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', )

class ReviewSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', )

class ReviewListSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'