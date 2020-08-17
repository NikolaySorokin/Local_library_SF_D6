from django import forms

from .models import Book, Author


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'
