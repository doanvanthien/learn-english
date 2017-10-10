# coding: utf8
from django import template
from django.template import Template
from django.shortcuts import render
from django.http import HttpResponse
from luyentu.models import words

def index(request):
	
	return render(request, 'index.html')
