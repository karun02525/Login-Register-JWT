from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=10)
    desc=models.CharField(max_length=20)
    price = models.IntegerField()
    
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=50)
        

class Book(models.Model):
    category  = models.ForeignKey(Category,on_delete=models.CASCADE)     
    book_title = models.CharField(max_length=100)  