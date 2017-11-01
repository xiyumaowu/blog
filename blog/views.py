# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return render(request, 'index.html')

def ui_elements(request):
	return render(request, 'ui-elements.html')

def chart(request):
	return render(request, 'chart.html')

def tab_panel(request):
	return render(request, 'tab-panel.html')

def table(request):
	return render(request, 'table.html')

def empty(request):
	return render(request, 'empty.html')

def form(request):
	return render(request, 'form.html')
