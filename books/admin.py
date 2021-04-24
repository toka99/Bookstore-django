from django.contrib import admin
from .models import Book , Category , Metric , Tag , Isbn
from .forms import BookForm
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title" , "author" , "content")
    list_filter = ("categories" , )
    search_fields = ("title" , )
    # readonly_fields = ("author" , )


class BookInLine(admin.StackedInline):
    model = Book
    max_num =3 
    extre =1 

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInLine]

admin.site.register(Book , BookAdmin)
admin.site.register(Category)
admin.site.register(Metric)
admin.site.register(Isbn)
admin.site.register(Tag , TagAdmin )

