from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Books

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"