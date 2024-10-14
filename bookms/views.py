from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView,TemplateView,DetailView
from django.urls import reverse_lazy

from .models import BookModel,Borrow
from .Forms.book_status_form import BookStatusForm
from .Forms.form import BookForm
from .Forms.borrow_form import BorrowForm
from .table import BookTable
from django.contrib.auth.models import User
from django.urls import reverse





# Create your views here.

class AddBookView(CreateView):
    model=BookModel
    form_class = BookForm
    templates_name='bookmodel_form.html'
    success_url = reverse_lazy('bookms:book_list')


class NavbarView(CreateView):
    def get(self, request):
        return render(request, 'bookms/navbar.html')
    

class BookListView(ListView):
    model = BookModel
    template_name = 'bookms/book_list.html'  
    context_object_name = 'book_table'  

    def get_queryset(self):
        return BookModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_table'] = BookTable(self.get_queryset())
        return context


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
    


class BorrowBookView(CreateView):
    model = Borrow
    form_class = BorrowForm 
    template_name = 'bookms/borrow_book.html'

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.kwargs.get('book_id')
        initial['book'] = get_object_or_404(BookModel, id=book_id)
        return initial
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_id = self.kwargs.get('book_id')
        context['book'] = get_object_or_404(BookModel, id=book_id)
        return context
    
    def get_success_url(self):
        instance = self.object
        return reverse_lazy('bookms:borrow_confirm',kwargs={'borrow_id':instance.id})
    

class ConfirmBookView(CreateView):
    model=Borrow
    form_class = BorrowForm 
    template_name= 'bookms/borrow_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        borrow_id = self.kwargs.get('borrow_id')
        context['borrow_entry'] = get_object_or_404(Borrow, id=borrow_id)
        return context
    

class BorrowedBooksListView(TemplateView):
    template_name = 'bookms/borrowed_books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(borrow__isnull=False).distinct()
        user_id = self.request.GET.get('user_id')
        
        if user_id:
            selected_user = get_object_or_404(User, id=user_id)
            context['selected_user'] = selected_user
            context['borrowed_books'] = Borrow.objects.filter(borrowed_by=selected_user)
        else:
            context['borrowed_books'] = None

        return context
    

class ReturnBookView(TemplateView):
    template_name ='bookms/return_book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
class ReturnBookDetailView(DetailView):
    model = Borrow
    template_name = 'bookms/return_book_detail.html'
    context_object_name = 'borrow_entry'
    pk_url_kwarg = 'borrow_id'


class MarkBookStatusView(UpdateView):
    model = BookModel
    template_name = 'bookms/return_book_detail.html'
    context_object_name = 'borrow_entry'
    form_class = BookStatusForm

    def get_success_url(self):
        
        return reverse('bookms:remove_book')  

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context
   
class RemoveBookView(DeleteView):
    model = BookModel
    template_name = 'bookms/remove_book_confirm.html'
    success_url = reverse_lazy('bookms:book_list')

    def get_object(self, queryset=None):
        return get_object_or_404(BookModel, id=self.kwargs['book_id'])
    

class RemoveBookConfirmationView(DeleteView):
    model = BookModel  
    template_name = 'bookms/remove_book_confirm.html' 
    success_url = reverse_lazy('bookms:book_list')

    def get_object(self, queryset=None):
        """Override to get the book object to be deleted."""
        return get_object_or_404(BookModel, id=self.kwargs['book_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.get_object() 
        return context
    