from django import forms
from ..models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['name','price','version','author','publication_info','isbn']

        