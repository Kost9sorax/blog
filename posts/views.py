from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, ReviewCreateSerializer, ThirdSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(swagger_auto_schema(request_body=ReviewCreateSerializer))
    @action(detail=True, methods=['POST'])
    def set_comment(self, request, pk=None):
        obj = get_object_or_404(Comment, pk=pk)
        serializer = ReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(obj)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()


class ThirdViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ThirdSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


