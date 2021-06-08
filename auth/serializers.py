from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from auth.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['email'], email=validated_data['email'])
        password = validated_data.pop('password')
        user.set_password(password)
        user.save()
        validated_data['user_id'] = user.id
        profile_ob = super(UserProfileSerializer, self).create(validated_data)
        return profile_ob

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'dob', 'type', 'password']


class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']