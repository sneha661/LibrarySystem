import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import BookModel

class BookTable(tables.Table):
    Action = tables.Column(empty_values=())

    class Meta:
        model = BookModel
        template_name = "django_tables2/bootstrap4.html"
        fields = ("id", "name", "price", "author","version","publication_info","isbn","Action")

    def render_Action(self, record):
        # Include the app namespace in the reverse call
        update_url = reverse('bookms:book_update', args=[record.id])
        delete_url = reverse('bookms:book_delete', args=[record.id])

        return format_html(
            f'''
            <a href="{update_url}" class="btn btn-sm btn-primary">Update</a> 
            <a href="{delete_url}" class="btn btn-sm btn-danger">Delete</a>
            '''
        )
