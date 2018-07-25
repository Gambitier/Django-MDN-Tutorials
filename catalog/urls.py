from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('book-detail', views.BookDetailView.as_view()),
    path('author-detail', views.AuthorDetailView.as_view()),
]

