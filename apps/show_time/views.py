# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    time = {
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime() )
    }
    print time
    return render(request, 'show_time/index.html', time)

def show(request):
    return redirect('/')

# Create your views here.
