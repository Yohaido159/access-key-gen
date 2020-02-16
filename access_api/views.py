from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.views.generic import TemplateView

from django.shortcuts import render
from .models import Post
from .serializers import SerializerPosts
from users.serializers import SerializerUser

from users.models import User, UserManager
from .logic.rand import set_to_user
from .permissions import IsCanAccess


class Index(TemplateView):
    template_name = "access_api/index.html"


class ListPosts(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = SerializerPosts
    permission_classes = (IsCanAccess,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        user = self.request.user
        print(user)
        # if user.id  != None:
        # set_to_user(user)
        #     pass
        return Response(serializer.data)


class Access(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SerializerUser


class GetAccess(generics.RetrieveAPIView):
    pass


class GenAccessKey(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = SerializerPosts

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        user = self.request.user
        if user.id != None:
            set_to_user(user, instance)
        return Response(serializer.data)

