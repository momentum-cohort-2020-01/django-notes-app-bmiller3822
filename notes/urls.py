"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.notes_list, name='notes-list'), #Has to align with HTML file
    path('notes/create/', views.new_note, name='new-note'), #Has to align with HTML file
    path('notes/<int:pk>', views.notes_detail, name="notes-detail"), #Has to align with HTML file
    path('admin/', admin.site.urls)
]


#First failed attempt.
# urlpatterns += [   
#     path('notes/create/', views.new_note, name='create-note'),  #No way this is right.  I'm going to have to redirect to a new endpoint.  Maybe another .html page?
# ]




