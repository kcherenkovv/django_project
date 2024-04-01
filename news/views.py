from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm

def news_home(request):
    news = Notes.objects.all().order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = NotesForm
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'news/create.html', data)

