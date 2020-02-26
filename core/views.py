from django.shortcuts import render
from django.http import HttpResponse

from .models import Note

def notes_list(request):
    notes = Note.objects.all() #We need to do something a lot, i.e. get all objects, so here's a method
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk) #primary key
    return render (request, 'core/notes_detail.html', {'note': note})


  # return HttpResponse("Hello, world. You're at the core index.")