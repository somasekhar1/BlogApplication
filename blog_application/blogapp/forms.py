from django import forms
from blogapp.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'published_date', 'description',)
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        
        # Check if a book with similar title and author already exists
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError('This book already exists.')

        return cleaned_data
