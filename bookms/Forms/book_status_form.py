
from django import forms
from ..models import BookModel 

class BookStatusForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['status'] 
        