from django.db import models
from address.models import AddressField

class CustomAddress(models.Model):
    address1 = AddressField()
    address_2 = AddressField(related_name='+', blank=True, null=True)
    
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=500)
    address = models.ForeignKey(CustomAddress, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self):
        return self.name
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=500)
    address = models.ForeignKey(CustomAddress, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    

class Book(models.Model):
    name = models.CharField(max_length=500)
    isbn = models.CharField(max_length=13)
    image = models.ImageField(upload_to='./static/images', null=True)
    preview = models.FileField(upload_to='./static/previews', null=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
