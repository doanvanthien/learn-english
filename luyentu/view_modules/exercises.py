#coding: utf-8
from luyentu.models import words, modules
from django.http import HttpResponse
import json, time
from random import randint
from django import template
from django.db.models import Q


def get_word(request=None):
	data = {}
	filters = []
	if request and request.body:
		#from second loads
		data_recv = json.loads(request.body)
	else:
		data_recv = {'en': 'Server been not recviced data', 'vi': 'Server không nhận được dữ liệu gửi lên', 'filter': ''}
	data_recv['en'] = data_recv['en'].strip()
	print "Từ cũ: ", data_recv['en'].encode('utf8')
	print data_recv
	filters = data_recv['filter'].split(';') if data_recv['filter'] != "" else []
	print filters
	old_word = words.objects.filter(en=data_recv['en'].strip())
	if old_word.count():
		data['old'] = {'en': data_recv['en'], 'vi': old_word[0].vi + "<br>" + data_recv['vi']}
	else:
		data['old'] = {'en': data_recv['en'], 'vi': "N/A<br>" + data_recv['vi']}
	
	new_word = random_choice_word(filters)
	
	data['new'] = {'en': new_word.en}
	print "Từ mới: ", new_word.en.encode('utf8')
	return HttpResponse(json.dumps(data))


def exercises(request):
	tp = template.loader.get_template('luyentu.html')
	categories = list( words.objects.values('categories').distinct())
	param_categories = []

	for category in categories:
		param_categories.append (category['categories'] )
	
	param = {
		'param': {
			'now': int(time.time()),
			'categories' : param_categories,
		}
	}
	return HttpResponse(tp.render(param, request))


def random_choice_word(filters):
	string_code = ''
	print "filter: ", filters
	pk_max = words.objects.order_by('-pk')[0].pk
	print not len(filters)
	if not len(filters):
		while True:
			w = words.objects.filter(pk=randint(0,pk_max))
			if w.count():
				break
		return w[0]

	for condition in filters:
		string_code += 'Q(categories="'+condition+'") | ' 
	string_code = string_code[:-2]
	print string_code
	w = words.objects.filter(eval(string_code))
	return w[randint(0, len(w) - 1)]


