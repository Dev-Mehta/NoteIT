from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Event
from .forms import CreateNoteForm, SignupForm
from datetime import date, datetime, time, timedelta
def home(request, newContext={}):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            task_name = form.cleaned_data.get('task_name')
            task_detail = form.cleaned_data.get('task_detail')
            event_time = form.cleaned_data.get('event_time')
            event_date = form.cleaned_data.get('event_date')
            today = date.today()
            now = datetime.now() + timedelta(minutes=10)
            now = now.time()
            category = form.cleaned_data.get('category')
            if event_date < today:
                messages.warning(request, "Some error in Date")
                return redirect('home')
            if event_time < now:
                messages.warning(request, "You need to get it done right now")
                e = Event(
                user=user,
                task_name=task_name,
                task_detail=task_detail,
                event_date=event_date,
                event_time=event_time,
                category=category
                ).save()
                messages.success(request, 'Note created successfully')
                return redirect('home')
            e = Event(
                user=user,
                task_name=task_name,
                task_detail=task_detail,
                event_date=event_date,
                event_time=event_time,
                category=category,
            ).save()
            messages.success(request, 'Note created successfully')
            return redirect('home')
        else:
            messages.warning(request, f"{form.errors}")
            return redirect('home')
    else:
        data = Event.objects.filter(user=request.user).order_by('-event_date','-event_time')
        form = CreateNoteForm()
        return render(request, "index.html",{"tasks":data,"form":form})
def DeleteNote(request, pk):
    note = Event.objects.get(id=pk)
    note.delete()
    return redirect('home')