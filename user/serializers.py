from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    role = GroupSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), write_only=True, source='role')

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'role', 'role_id', 'language', 'created_at']
        read_only_fields = ['created_at']
