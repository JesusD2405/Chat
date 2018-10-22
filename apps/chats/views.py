from django.shortcuts import render, redirect
#from django.http import HttpResponseRedirect
#from django.urls import reverse_lazy
#from django.core import serializers
#from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })