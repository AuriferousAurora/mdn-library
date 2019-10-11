from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, BookInstance, Genre

def index(request):
  """View function for home page of site."""
  
  # Generate counts of some of the main objects.
  num_books = Book.objects.count()
  num_instances = BookInstance.objects.count()
  num_instances_available = BookInstance.objects.filter(status__exact='a').count()
  num_authors = Author.objects.count()
  harry_potter_books = Book.objects.filter(title__icontains='Harry Potter')
  num_harry_potter_books = harry_potter_books.count()

  num_harry_potter_books_available = 0
  for book in harry_potter_books:
    instances = BookInstance.objects.filter(book=book)
    for instance in instances:
      if instance.status == 'a':
        num_harry_potter_books_available = num_harry_potter_books_available + 1
      else:
        print(instance.status)



  context = {
    'num_books': num_books,
    'num_instances': num_instances,
    'num_instances_available': num_instances_available,
    'num_authors': num_authors,
    'num_harry_potter_books': num_harry_potter_books,
    'num_harry_potter_books_available': num_harry_potter_books_available,
  }

  return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
  model = Book
  paginate_by = 10


class BookDetailView(generic.DetailView):
  model = Book


class AuthorListView(generic.ListView):
  model = Author
  paginate_by = 10


class AuthorDetailView(generic.DetailView):
  model = Author

