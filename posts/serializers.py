from rest_framework import serializers
from .models import Post, Comment


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterReviewListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ThirdFilterListSerializer(serializers.ListSerializer):
    def to_rep(self, data):
        first_lvl = data.filter(parent=None)
        second_lvl = data.filter(parent=first_lvl)
        third_lvl = data.filter(parent=second_lvl)
        return CommentSerializer(third_lvl.data, many=True)


class CommentThirdSerializer(serializers.ModelSerializer):
    children = None

    class Meta:
        list_serializer_class = ThirdFilterListSerializer
        model = Comment
        fields = ['id', 'body', 'post', 'parent', 'children']


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Comment
        fields = ['id', 'body', 'post', 'parent', 'children']


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'parent', 'post']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'comments']


class ThirdSerializer(serializers.ModelSerializer):
    comments = CommentThirdSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'comments']
