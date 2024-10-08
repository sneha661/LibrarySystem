
from django.db import models
from django.contrib.auth.models import User

class BookModel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    version=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_info=models.CharField(max_length=100, null=True)
    isbn=models.CharField(max_length=100, null=True)
    
    #presentation of model....
    def __str__(self) -> str:
        return self.name
    

class BookCopy(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('lost', 'Lost'), ('damaged', 'Damaged')], default='available')
    borrowed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.book
