from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("login/", UserLogin.as_view()),
    path("snippet/", SnippetDetails.as_view()),
    path("snippet/<int:pk>/", SnippetDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)