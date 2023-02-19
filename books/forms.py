from django import forms
from django.core.exceptions import ValidationError

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

    def clean(self):
        self.cleaned_data = super().clean()

        if not self.cleaned_data.get('image') and not self.cleaned_data.get('preview'):
            raise ValidationError('Insire una imagine e una preview.')

        return self.cleaned_data