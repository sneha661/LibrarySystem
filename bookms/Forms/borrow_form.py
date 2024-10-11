

from django import forms
from ..models import Borrow, BookModel
from django.contrib.auth.models import User

class BorrowForm(forms.ModelForm):
    borrowed_by = forms.ModelChoiceField(queryset=User.objects.all(), label="Borrowed By")
    book = forms.ModelChoiceField(queryset=BookModel.objects.all())

    class Meta:
        model = Borrow  
        fields = ['borrowed_by','book']  

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].widget.attrs ={'hidden':True}