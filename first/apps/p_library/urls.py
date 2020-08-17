from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import BooksList, PublishersList, \
    BookDetail, BookCreate, \
    BookUpdate, AuthorList, \
    AuthorDetail, FriendsList, \
    FriendDetail, AuthorCreate, \
    AuthorUpdate
from . import views


app_name = "p_library"
urlpatterns = [
    path("", views.index),
    path("library/", BooksList.as_view(), name="books_list"),
    path("library/<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path("library/book/create", BookCreate.as_view(), name="book_create"),
    path("library/book/edit/<int:pk>/", BookUpdate.as_view(), name="book_update"),
    path("library/book_increment/", views.book_increment, name="book_increment"),
    path("library/book_decrement/", views.book_decrement, name="book_decrement"),
    path("library/authors/", AuthorList.as_view(), name="authors_list"),
    path("library/author/<int:pk>/", AuthorDetail.as_view(), name="author_detail"),
    path("library/author/create", AuthorCreate.as_view(), name="author_create"),
    path("library/author/edit/<int:pk>/", AuthorUpdate.as_view(), name="author_update"),
    path("library/publishers/", PublishersList.as_view(), name="publishers"),
    path("library/friends/", FriendsList.as_view(), name="friends_list"),
    path("library/friend/<int:pk>/", FriendDetail.as_view(), name="friend_detail")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
