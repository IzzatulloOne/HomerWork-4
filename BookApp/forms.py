# BookApp/forms.py
from django import forms
from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100)
    author = forms.CharField(label='Автор', max_length=100)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    cover_image = forms.ImageField(label='Обложка книги')
    
    def save(self):
        data = self.cleaned_data
        book = Book(
            title=data['title'],
            author=data['author'],
            description=data['description'],
            cover_image=data['cover_image']  
        )
        book.save()
        return book
