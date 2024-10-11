
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
    

class Borrow(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    other_details = models.TextField(blank=True, null=True)  
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False) 
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Book {self.book.name} borrowed by {self.borrowed_by}"
    

