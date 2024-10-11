import django_tables2 as tables
from .models import BookModel

class BookTable(tables.Table):
    Action = tables.TemplateColumn(
        template_code='''
            <a href="{% url 'bookms:book_update' record.id %}" class="btn btn-sm btn-primary">Update</a>
            <a href="{% url 'bookms:book_delete' record.id %}" class="btn btn-sm btn-danger">Delete</a>
            <a href="{% url 'bookms:book_borrow' record.id %}" class="btn btn-sm btn-warning">Borrow</a>
        '''
        
    )

    class Meta:
        model = BookModel
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "price", "author", "version", "publication_info", "isbn", "Action")
