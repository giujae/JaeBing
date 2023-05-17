from rest_framework import serializers
from .models import Board, Comment
from django.contrib.auth import get_user_model

# user info
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

# community detail
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id','user','title','content','board_code','created_at','updated_at')

# community create user
class BoardUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    class Meta:
        model = Board
        fields = ('id','user','title','content','board_code','created_at','updated_at')

# community comment create
class BoardCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','user','board','content','created_at','updated_at')

# community comment create user 
class BoardCommentUserSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()
    board = BoardSerializer()
    class Meta:
        model = Comment
        fields = ('id','user','board','content','created_at','updated_at')