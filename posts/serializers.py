from rest_framework import serializers
from .models import Post, Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'post', 'parent', 'children']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'comments']
