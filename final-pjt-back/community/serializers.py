from rest_framework import serializers
from .models import Review, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user')

class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'