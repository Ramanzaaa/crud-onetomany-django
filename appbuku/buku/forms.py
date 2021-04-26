from django import forms
from .models import Buku,Author
#DataFlair
class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nama']
