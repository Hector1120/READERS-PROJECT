from django.shortcuts import render, redirect, get_object_or_404
from .models import Books
from .forms import BookForm

# Vista para listar los libros
def book_list(request):
    books = Books.objects.all()
    return render(request, 'readings/listBook.html', {'books': books})

# Vista para crear un nuevo libro
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'readings/createBook.html', {'form': form})

# Vista para actualizar un libro existente
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'readings/createBook.html', {'form': form})

# Vista para eliminar un libro
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'readings/book_confirm_delete.html', {'book': book})
