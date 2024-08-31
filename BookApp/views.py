from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.http import Http404

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id): # ustoz manu she yerda get_object_or_404 ishlatishim avzalroq edi lekin man shu get_object_or_404 ishlatishdi error lar chiqqani uchun ishlatmadim 
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404("Книга не найдена")
    
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def page_one(request):
    return render(request, 'page_one.html')

def page_two(request):
    return render(request, 'page_two.html')

def page_three(request):
    return render(request, 'page_three.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('home')
    else:
        form = BookForm()
    
    return render(request, 'add_book.html', {'form': form})
