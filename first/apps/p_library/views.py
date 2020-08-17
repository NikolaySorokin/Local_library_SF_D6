from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.template import loader

from .models import Book, Author, Publisher, Friend
from .forms import BookForm, AuthorForm


def index(request):
    template = loader.get_template('p_library/index.html')
    biblio_data = {
        'books_count': str(Book.objects.count())
    }
    return HttpResponse(template.render(biblio_data, request))


class BooksList(ListView):
    model = Book
    template_name = 'p_library/books_list.html'
    context_object_name = 'books_list'

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            book.copy_count += 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/library/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/library/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/library/')
    else:
        return redirect('/library/')


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreate(CreateView):
    model = Book
    form_class = BookForm


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm


class AuthorList(ListView):
    model = Author
    template_name = 'p_library/authors_list.html'
    context_object_name = 'authors_list'


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'


class AuthorCreate(CreateView):
    model = Author
    form_class = AuthorForm


class AuthorUpdate(UpdateView):
    model = Author
    form_class = AuthorForm


class PublishersList(ListView):
    model = Publisher
    template_name = 'p_library/publishers.html'
    context_object_name = 'publishers'


class FriendsList(ListView):
    model = Friend
    template_name = 'p_library/friends_list.html'
    context_object_name = 'friends_list'


class FriendDetail(DetailView):
    model = Friend
    context_object_name = 'friend'
