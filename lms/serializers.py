from dataclasses import fields
import email
from django.contrib.auth.models import User
from  rest_framework import serializers, validators
from .models import Books

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username', 'password','email','is_staff')

        extra_kwargs={
            'password':{'write_only':True},
            'email':{
                'required':True,
                'allow_blank':False,
                'validators':[validators.UniqueValidator(
                    User.objects.all(),'A user with that email already exists'
                )
                ]
            }
        }
    def create(self, validated_data):
        username=validated_data.get('username')
        password=validated_data.get('password')
        email=validated_data.get('email')
        is_staff=validated_data.get('is_staff')

        user=User.objects.create(
            username=username,
            password=password,
            email=email,
            is_staff=is_staff,
        )
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books
        fields="__all__"