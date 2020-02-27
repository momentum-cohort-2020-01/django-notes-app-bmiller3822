import datetime

# from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Note
from .forms import NewNoteForm

# @permission_required('catalog.can_mark_returned')     Maybe we'll use this later?
def notes_list(request):
    notes = Note.objects.all() 
    return render(request, 'core/notes_list.html', {'notes': notes})

def notes_detail(request, pk):
    note = Note.objects.get(pk=pk) 
    return render (request, 'core/notes_detail.html', {'note': note})

def new_note(request):
    # note_instance = get_object_or_404(pk=pk) #Pretty sure this is wrong.   NoteInstance (argument)
    if request.method == 'POST':
        form = NewNoteForm(request.POST)
        if form.is_valid():   
            note = form.save()
            return redirect('notes-detail', pk=note.pk)
    else:
        form = NewNoteForm()
    return render (request, 'core/new_note.html', {"form": form})

def note_edit(request, pk):
    # note = Note.objects.get(pk=pk)
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NewNoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save
            form.save()
            return redirect('notes-list')
    else:
        form = NewNoteForm(instance=note)
    return render (request, 'core/note_edit.html', {'form': form})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('notes-list')

# def delete_edit(request, pk):
#     note = Note.objects.get(pk=pk)
#     if request.method == "DELETE":
#         form = NewNoteForm(request.POST, instance=note)
#         if form.is_valid():
#             note = form.save
#             form.save()
#             return redirect('notes-list')
#     else:
#         form = NewNoteForm(instance=note)
#     return render (request, 'core/note_edit.html', {'form': form})


#First failed attempt (Might come back to this)
    # if request.method == "POST":
    #     form = NewNoteForm(request.POST)
    #     if form.is_valid():
    #         note_instance = form.cleaned_data['note_text']
    #         note_instance.save()
    #         return HttpResponseRedirect(reverse('notes_list') )
    # else: 
    #     proposed_note = "Please enter a note."
    #     form = NewNoteForm(initial={'note_text': "Enter note here."})
    
    # context = {
    #     'form': form,
    #     'note_instance': note_instance,
    # }

    # return render (request, 'core/new_note.html', context)


# Come back to commit = false ***** Intermediate step to do stuff with the data.


  # return HttpResponse("Hello, world. You're at the core index.")

  #Can also be written as:
  #def notes_list(request):
  #notes = Note.objects.all()
  #context = {'notes': notes}
  #return render(request, 'core/notes_list.html', context)