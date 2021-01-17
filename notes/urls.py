from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', login_required(views.home), name='home'),
    path('delete/note/<int:pk>', login_required(views.DeleteNote), name='delete_note')
]