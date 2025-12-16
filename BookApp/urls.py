from django.urls import path
from .views import BookListApiView, BookCreateApiView, BookDeleteApiView, BookDetailApiView, BookUpdateApiView, BookMixApiView

urlpatterns = [
    path('books/', BookListApiView.as_view(), name='books'),
    path('books/create/', BookCreateApiView.as_view(), name='books-create'),
    path('books/delete/<int:pk>', BookDeleteApiView.as_view(), name='books-delete'),
    path('books/detail/<int:pk>', BookDetailApiView.as_view(), name='books-detail'),
    path('books/update/<int:pk>', BookUpdateApiView.as_view(), name='books-update'),
    path('books/mix/<int:pk>', BookMixApiView.as_view(), name='books-mix'),

]