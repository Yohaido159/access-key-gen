from rest_framework import serializers
from .models import Post

class SerializerPosts(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id" , "title" , "body")

        

