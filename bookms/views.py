from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy,reverse

from .models import BookModel
from .form import BookForm 
from .table import BookTable

from datetime import date, timedelta
from .models import BookCopy
from django.contrib import messages
from django.utils import timezone
# Create your views here.

class AddBookView(CreateView):
    model=BookModel
    form_class = BookForm
    templates_name='bookmodel_form.html'
    success_url = reverse_lazy('bookms:book_list')


def navbar(request):
    return render(request, 'bookms/navbar.html')


def book_list(request):
    books = BookModel.objects.all()  
    book_table = BookTable(books)  
    return render(request, 'bookms/book_list.html', {
        'book_table': book_table 
    })


class BookUpdateView(UpdateView):
    model= BookModel
    form_class=BookForm
    template_name='bookms/update_book.html'
    success_url = reverse_lazy('bookms:book_list')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['book'] = self.get_object()
        return context

class BookDeleteView(DeleteView):
    model = BookModel
    template_name = 'bookms/delete_book.html'
    success_url = reverse_lazy('bookms:book_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.get_object()
        return context

class BookBorrowView(DetailView):
    model = BookCopy
    template_name = 'book_detail.html'  
    context_object_name = 'book_copy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.get_object()  
        return context

    def post(self, request, *args, **kwargs):
        book_copy = get_object_or_404(BookCopy, id=self.kwargs['pk'])  # Ensure we get the correct book copy

        if book_copy.status == 'available':
            book_copy.status = 'borrowed'
            book_copy.borrowed_by = request.user
            book_copy.due_date = timezone.now().date() + timedelta(days=14)
            book_copy.save()
            
            messages.success(request, f'You have borrowed "{book_copy.book.name}". Due date is {book_copy.due_date}.')
        else:
            messages.error(request, 'This book is currently unavailable.')
        
        return redirect('bookms:book_list')