from django.urls import path
from .views import home_view, articles_view, articles_view_detail, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('articles/', articles_view, name='articles'),
    path('articles/<int:pk>/', articles_view_detail, name='articles_detail'),
]
