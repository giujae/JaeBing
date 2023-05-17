from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from .models import Board, Comment
from .serializers import UserInfoSerializer,BoardSerializer,BoardUserSerializer,BoardCommentSerializer,BoardCommentUserSerializer

from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# ---------------------------------community---------------------------------
# community 
@api_view(['GET'])
def index(request):
    boards = Board.objects.order_by('-pk')
    serializer = BoardUserSerializer(boards, many=True)
    return Response(serializer.data, safe=False)

# community C(create)
@api_view(['POST'])
def create(request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# community R(detail)
@api_view(['GET'])
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    serializer = BoardUserSerializer(board)
    return Response(serializer.data, safe=False)

# community UD(update & delete)
@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def update_delete(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'DELETE' :
        serializer = BoardUserSerializer(board)
        if request.user.is_superuser or board.user == request.user :
            board.delete()
        return Response(True)
    else :
        if board.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = BoardSerializer(board, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        
# ---------------------------------comment---------------------------------
@api_view(['GET'])
def comment_list(request, board_pk):
    comments = Comment.objects.order_by('pk').filter(board_id=board_pk)
    serializer = BoardCommentUserSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def comment_create(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    commentItem = request.data
    comment = Comment(
        board = board,
        user = request.user,
        content = commentItem['content'],
    )
    comment.save()
    serializer = BoardCommentUserSerializer(comment)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, board_pk, comment_pk):
    board = get_object_or_404(Board, pk=board_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    commentId = comment.id
    if request.method == 'DELETE' :
        serializer = BoardCommentSerializer(comment)
        if request.user.is_superuser or board.user == request.user :
            comment.delete()
        return Response({'id':commentId})
    else :
        if comment.user == request.user : 
            request.data['user'] = request.user.pk
            serializer = BoardCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else : 
                return Response(False)
            

