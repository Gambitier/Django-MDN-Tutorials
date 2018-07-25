from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):

    def get(self, request):
        welcome = "Welcome to index page"
        return HttpResponse(welcome)


class BookDetailView(View):

    def get(self, request):
        msg = "This is a page to show Book Details"
        return HttpResponse(msg)


class AuthorDetailView(View):

    def get(self, request):
        msg = "This is a page to show Author Details"
        return HttpResponse(msg)