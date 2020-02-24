from django.shortcuts import render
from django.http import HttpResponse

import data

# Create your views here.
def index(request):
    notes = data.NOTES
    return render(request, 'base.html', {'notes': notes})
    # return HttpResponse("Hello, world. You're at the core index.")