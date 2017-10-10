from django.db.models import Q
from luyentu.models import *

def auto_make_code(filters):
	string_code = ''
	for condition in filters:
		string_code += 'Q(categories="'+condition+'") | ' 
	string_code = string_code[:-2]
	print string_code
	w = words.objects.filter(eval(string_code))
	return w