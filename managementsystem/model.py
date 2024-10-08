from django.db import models

"""
Model for book..
"""


class BookModel(models.Model):
    
    name=models.CharField(max_length=100)
    price=models.IntegerField(max_length=20)
    


