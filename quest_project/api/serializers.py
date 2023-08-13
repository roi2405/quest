from rest_framework import serializers
from .models import User, get_all_class_fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('city', 'education', 'name')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = get_all_class_fields(User)
        fields = ('city', 'education', 'name')