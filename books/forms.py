from django import forms
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        exclude = ("metrics",)


        
    def clean_title(self):
        title=self.cleaned_data.get("title")
        if "test" in title:
            raise ValidationError("title shouldn't has test word!")
        return title 

        
    def clean(self):
        super(BookForm , self).clean()
        content = self.cleaned_data.get('content')
        title = self.cleaned_data.get('title')

        if len(content) < 10:
            raise ValidationError("content must be longer than 10 chars")

        return self.cleaned_data

