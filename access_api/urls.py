from django.urls import path, include
from .views import ListPosts, Access , GetAccess, GenAccessKey

urlpatterns = [
    path("list/<int:pk>", ListPosts.as_view(), name="post-list-api"),
    path("user/<int:pk>", Access.as_view(), name="user-list-api"),
    
    path("get/<int:pk>", GetAccess.as_view(), name="get-access-api"),
    path("gen_access/<int:pk>", GenAccessKey.as_view(), name="get-access-api"),

    # path("api_auth/", include("rest_framework.urls")),
    # path("rest_auth/", include("rest_auth.urls")),
    # path("rest-auth/registration/", include("rest_auth.registration.urls")),


]
