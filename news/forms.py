from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'full_text','date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заметки'
            }),
            'description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание заметки'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заметки'
            }),
        }