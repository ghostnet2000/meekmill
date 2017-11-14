import copy
import logging

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets, generics
from rest_framework.response import Response

from .form import BookForm
from .models import Book, Tag
from .serializers import BookSerializer


LOGGER = logging.getLogger(__name__)

# *************************************************************************
# ***************************** Django views ******************************
# *************************************************************************


def index(request):
    """Index view.

    :param request:
    :type request: django.http.HttpRequest
    :return:
    :rtype: django.http.HttpResponse
    """
    all_books = Book.objects.all()

    context = {
        'all_books': all_books
    }
    return render(request, 'index.html', context)


def detail(request, book_id):
    """Detail view.

    :param request:
    :param book_id:
    :type request: django.http.HttpRequest
    :type book_id: int
    :return:
    :rtype: django.http.HttpResponse
    """
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist as err:
        raise Http404(_("Not found!"))

    context = {
        'books': book
    }
    return render(request, 'detail.html', context)


def delete_book(request, book_id):
    """Delete book view.

    :param request:
    :param book_id:
    :type request: django.http.HttpRequest
    :type book_id: int
    :return:
    :rtype: django.http.HttpResponse
    """
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist as err:
        raise Http404(_("Not found!"))

    book.delete()
    messages.success(request, _('Book successfully deleted.'))
    return redirect(reverse('books:index'))


def create(request):
    """Create book view.

    :param request:
    :type request: django.http.HttpRequest
    :return:
    :rtype: django.http.HttpResponse
    """
    LOGGER.debug("create called")

    if request.method == 'POST':
        book_form = BookForm(data=request.POST,
                                 files=request.FILES,
                                 prefix='book')

        if book_form.is_valid():
            book = book_form.save()

            messages.success(request, _('Book successfully created.'))

            return redirect(reverse('books:index'))

    else:
        book_form = BookForm(prefix='book')

    context = {
        'book_form': book_form,
    }

    return render(request, 'create.html', context)


# *************************************************************************
# ******************** API (Django REST framework) views ******************
# *************************************************************************

class BookViewSet(viewsets.ModelViewSet):
    """Book view set."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SearchView(generics.ListAPIView):
    """Search view set."""

    serializer_class = BookSerializer

    def get_queryset(self):
        parameter = self.request.GET.get('q', default='')
        return Book.objects.filter(title__icontains=parameter)


class ByTagView(generics.ListAPIView):
    """Book by tag view set."""

    serializer_class = BookSerializer

    def get_queryset(self):
        tag_id = self.request.GET.get('id', default='')
        return Tag.objects.get(pk=tag_id).book_set.all()

    def list(self, request, *args, **kwargs):
        tag_id = request.GET.get('id', default='')
        queryset = self.get_queryset()
        serializer = BookSerializer(queryset, many=True)
        response_data = {
            'tag_name': Tag.objects.get(pk=tag_id).name,
            'books': serializer.data
        }
        return Response(response_data)
