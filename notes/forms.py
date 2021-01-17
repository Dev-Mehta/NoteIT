from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateNoteForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ['user','sent_reminder']
		widgets = {
			"event_date":forms.DateInput(attrs={'type':'date'}),
			"event_time":forms.DateInput(format='%H:%M',attrs={'type':'time'}),
		}


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email","password1","password2")