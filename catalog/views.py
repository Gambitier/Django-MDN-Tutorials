from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views import View


class IndexView(View):

    def get(self, request):
        # welcome = "Welcome to index page"
        # return HttpResponse(welcome)

        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
        num_instances_available = BookInstance.objects.filter(status__exact='a').count()
        num_authors = Author.objects.count()  # The 'all()' is implied by default.
        num_genres = Genre.objects.count()  # The 'all()' is implied by default.
        num_books_Guide = Book.objects.filter(title__icontains='Guide').count()
        context = {
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_Guide': num_books_Guide,
        }
        return render(request, 'catalog/index.html', context)


class BookView(View):

    def get(self, request):
        msg = "List of Books"
        return HttpResponse(msg)


class AuthorView(View):

    def get(self, request):
        msg = "List of Authors"
        return HttpResponse(msg)


class BookDetailsView(View):

    def get(self, request, id):
        msg = "This is a page to show Book Details  Book: "
        return HttpResponse(msg + "<br> <br/> Book:" + id)


class AuthorDetailsView(View):

    def get(self, request, id):
        msg = "This is a page to show Author Details"
        return HttpResponse(msg + "<br/><br/>Author: " + id)
