from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow, User


from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = CharField()

    class Meta:
        model = Follow
        fields = '__all__'

    def validate_following(self, value):
        return get_object_or_404(User, username=value)

    def create(self, validated_data):
        user = validated_data.get('user')
        following = get_object_or_404(User,
                                      username=validated_data.get('following'))
        if Follow.objects.filter(following=following,
                                 user=user).exists():
            raise serializers.ValidationError('Уже подписан на данного '
                                              'пользователя!')
        if user.id == following.id:
            raise serializers.ValidationError('Нельзя подписаться '
                                              'самому на себя!')
        return super().create(validated_data)
