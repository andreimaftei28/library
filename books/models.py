from django.db import models
from address.models import AddressField

class CustomAddress(models.Model):
    address1 = AddressField()
    address_2 = AddressField(related_name='+', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Addresses"
    
class Subject(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Subjects"
        ordering = ("name", )
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=500)
    address = models.ForeignKey(CustomAddress, on_delete=models.PROTECT, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Authors"
        ordering = ("name", "address")
    
    def __str__(self):
        return self.name
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=500)
    address = models.ForeignKey(CustomAddress, on_delete=models.PROTECT, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Publishers"
        ordering = ("name", "address")
    
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

    class Meta:
        unique_together = ("name", "author", )
        ordering = ("name", "author")
    
    def __str__(self):
        return self.name
