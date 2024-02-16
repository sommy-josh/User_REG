from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import User
from rest_framework.request import Request
from .serializers import UserSerializer


class RegisterView(generics.GenericAPIView):
    serializer_class=UserSerializer

    def post(self,request:Request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()

            response={
                'message': 'user created successfully',
                'data': serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



