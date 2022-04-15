from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, ReviewCreateSerializer
from rest_framework.views import APIView


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ReviewCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ReviewCreateSerializer

    def perform_create(self, serializer):
        serializer.save()
