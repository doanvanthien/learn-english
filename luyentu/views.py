# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import template

# Create your views here.
from django.http import HttpResponse
from luyentu.models import words, modules
from random import randint
import time

# modules views
import view_modules as vm


def index(request):
	return vm.index(request)


def exercises(request):
	print dir(vm)
	return vm.exercises(request)


def update_modules(request):
	return vm.update_modules(request)


def get_word(request):	
	return vm.get_word(request)



	
def test_template(request):
	tp = template.loader.get_template('luyentu.html')
	count = words.objects.all().count()
	w = words.objects.get(pk=randint(1, count))
	param = {
		'param': {
			'now': int(time.time()),
		}
	}
	return HttpResponse(tp.render(param, request))


def test(request):
	response = HttpResponse()
	data1 = request.POST
	data1 = request.GET
	response.write(data1 + "<br>======<br>")
	response.write(data2)
	return response

def get(request):
	response = HttpResponse()
	count = words.objects.all().count()
	w = words.objects.get(pk=1)
	response.write(repr(w))
	return response
