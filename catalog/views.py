from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
from django.views import View, generic


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


class BookListView(generic.ListView):
    model = Book
    # =============================================================================== Within the template you can
    # access the list of books with the template variable named object_list OR book_list (i.e. generically
    # "the_model_name_list").
    #  ===============================================================================

    template_name = 'catalog/book_list.html'

    # context_object_name = 'my_book_list'
    # queryset = Book.objects.all()

    # ==================================================================================
    # we can override the  get_queryset() method to change the list of records returned. This is more flexible than
    # just setting the queryset attribute
    # ==================================================================================

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs

    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     return context


class AuthorListView(View):

    def get(self, request):
        msg = "List of Authors"
        return HttpResponse(msg)


class BookDetailsView(generic.DetailView):
    # ===============================================================================
    # If a requested record does not exist then the generic class-based detail view will raise an Http404 exception
    # for you automatically
    # ===============================================================================
    template_name = "catalog/book_detail.html"
    model = BookInstance
    # ===============================================================================
    # Within the template you can access the list of books with the
    # template variable named object OR book (i.e. generically "the_model_name").
    # ===============================================================================


class AuthorDetailsView(View):
    pass
