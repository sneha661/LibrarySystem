from django.contrib import admin
from django.urls import path
from .views import AddBookView, BookUpdateView, BookDeleteView,BookBorrowView
from . import views

app_name = 'bookms'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', AddBookView.as_view(), name='book-create'),
    path('list/', views.book_list, name='book_list'),
    path('nav/', views.navbar, name='navbar'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'), 
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    path('borrow/<int:pk>/', BookBorrowView.as_view(), name='borrow_book'),
]