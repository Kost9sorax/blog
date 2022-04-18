from django.core import serializers
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, ReviewCreateSerializer
from rest_framework.views import APIView

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @method_decorator(swagger_auto_schema(request_body=ReviewCreateSerializer))
    @action(detail=True, methods=['POST'])
    def set_comment(self, request, pk=None):
        comment = self.get_object()
        model = Comment
        get_object_or_404(model, pk=pk)
        serializer = ReviewCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'comment set'})


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
