from django.contrib import admin
from django.urls import path
from .views import AddBookView, BookUpdateView, BookDeleteView,BookListView,BorrowBookView,ConfirmBookView,BorrowedBooksListView,ReturnBookView,ReturnBookDetailView
from . import views

app_name = 'bookms'

urlpatterns = [
    path('create/', AddBookView.as_view(), name='book-create'),
    path('list/', BookListView.as_view(), name='book_list'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('<int:book_id>/borrow/',BorrowBookView.as_view(), name='book_borrow'), 
    path('borrow/<int:borrow_id>/confirm/',ConfirmBookView.as_view(), name='borrow_confirm'),
    path('borrowed_books/', BorrowedBooksListView.as_view(), name='borrowed_books_list'),
    path('return_book/<int:book_id>/', ReturnBookView.as_view(), name='return_book'),
    path('return_book/<int:borrow_id>/detail/', ReturnBookDetailView.as_view(), name='return_book_detail'),

]
