from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('books/', views.BookView.as_view(), name='books'),
    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('book/<str:id>/', views.BookDetailsView.as_view(), name="book details"),
    path('author/<str:id>/', views.AuthorDetailsView.as_view(), name="author details"),
]
