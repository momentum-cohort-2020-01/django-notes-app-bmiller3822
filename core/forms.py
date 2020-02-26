import datetime

from django import forms
from django.forms import ModelForm 
from .models import Note  
#MDN EXAMPLES FOR IMPORTS:
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
    
class NewNoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'body',)






#First failed attempt

    # note_text = forms.CharField(help_text="Enter your note here.")

    # def clean_note_text(self):
    #     data = self.cleaned_data['note_text']

    #     if len(data)>0:
    #         return data
    #     else:
    #         raise ValidationError(_('Please enter a note.'))
    #     return data  #Not sure if I need this or not.



# def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
        
#         # Check if a date is not in the past. 
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))

#         # Check if a date is in the allowed range (+4 weeks from today).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

#         # Remember to always return the cleaned data.
#         return data