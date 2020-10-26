from django.apps import AppConfig
from . models import Category, Post


class BlogConfig(AppConfig):
    name = 'blog'
