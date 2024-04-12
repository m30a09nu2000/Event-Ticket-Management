from django.contrib import admin
from django.urls import path, include
from .views import HomeView, RegisterView

urlpatterns = [
    path("home", HomeView.as_view()),
    path("register", RegisterView.as_view()),
]
