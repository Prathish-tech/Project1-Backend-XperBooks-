# Books/urls.py
from django.urls import path
from .views import BookView, BookDetail, TestView

urlpatterns = [
    path('', BookView.as_view(), name='book_list'),  # GET/POST for listing and creating books
    path('<int:pk>/', BookDetail.as_view(), name='book_detail'),  # GET/PUT/DELETE for individual book
    path('test/', TestView.as_view(), name='test_view'),
]
