from .models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

class UserSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=255)  # Assuming a reasonable maximum length
    password=serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password',]

    def validate(self, attrs):
    
        email_exists=User.objects.filter(email=attrs['email']).exists()
        if email_exists:
            raise ValidationError("Email has already been used")
        
        return super().validate(attrs)
        
    def create(self,validated_data):
        password=validated_data.pop("password")
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        return user