from django.urls import path
from .views import *

urlpatterns = [
    path('books/', BookListApiView.as_view()),
    path('books/create/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view()),
    path('books/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('books/delete/<int:pk>/', BookDeleteAPIView.as_view()),
    path('books/all/', BookListCreateAPIView.as_view()),
]