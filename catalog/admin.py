from django.contrib import admin

from catalog.models import Author, Book, BookInstance, Genre, Language

admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
  extra = 0
  model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
  fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
  inlines = [BookInline]

class BooksInstanceInline(admin.TabularInline):
  extra = 0
  model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'display_genre')
  inlines = [BooksInstanceInline]

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
  list_display = ('book', 'id', 'due_back', 'status')
  list_filter = ('status', 'due_back')

  fieldsets = (
    (None, {
      'fields': ('book', 'imprint', 'id')
    }),
    ('Availability', {
      'fields': ('status', 'due_back')
    }),
  )
