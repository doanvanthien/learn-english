# coding: utf-8

from django.http import HttpResponse, HttpRequest
from ..models import words, modules
import os, hashlib, codecs

def update_modules(request):
	_dir = os.path.realpath( os.getcwd() + '/luyentu/words')
	dict_hash = {}
	updated_list = {} # { module: [founded, num_lines_add], module: [founded, num_lines_add] } 
	response = None
	update_words = 0
	_debug = ''
	a = None
	for row in list(modules.objects.all()):
		dict_hash[row.hash_value] = row.module_name

	for file in os.listdir(_dir):
		updated_list[file] = [0, 0]
		_debug += file + " "
		path_file = os.path.realpath(_dir + '/' + file)
		if os.path.isfile( path_file ):
			f = codecs.open(path_file, mode='r', encoding='utf-8')
			data = f.read()
			updated_list[file][0] = len(data.split('\n'))
			hash_value = hashlib.md5(data.encode('utf-8')).hexdigest()
			f.close()
			if hash_value in dict_hash.keys():
				continue
			
			# add words
			dict_lines = data.split("\n")
			for line in dict_lines:
				# "1|hello|verb|Xin chao"
				# "status|en|category|vi"
				struct_line = line.split("|")
				if len(struct_line) != 4:
					continue
				categories = struct_line[2]
				categories = categories.replace("(", "")
				categories = categories.replace(")", "")
				categories = categories.split(",")
				for category in categories:
					category = category.strip()
					if not words.objects.filter(categories=category, en=struct_line[1], vi=struct_line[3]).count():
						new_word = words(state=int(struct_line[0]), en=struct_line[1], categories=category, vi=struct_line[3])
						update_words += 1
						updated_list[file][1] += 1
						new_word.save()
						_debug = "[" + str(update_words) + "] {0}|{1}|{2}|{3}" . format( str(new_word.state), new_word.en.encode('utf-8'), new_word.vi.encode('utf-8'), new_word.categories )
						print _debug
			# update module table
			m = modules.objects.filter(module_name=file)
			if m.count():
				module = m[0]
				module.hash_value = hash_value
			else:
				module = modules(hash_value=hash_value, module_name=file)
			module.save()
	str_tmp = ''
	for module in updated_list.keys():
			str_tmp += "<p>" + module + ": found: " + str(updated_list[module][0]) + " lines, updated: " + str(updated_list[module][1])+ " words</p>"
	print "str_tmp: ", str_tmp 
	if request!=None:
		response = HttpResponse()
		response.write("<h1>Updated_list </h2>")
		response.write("<br>")
		response.write(str_tmp)
		response.write("<br>")
		response.write('<a href="/luyentu/">Trang chủ</a>')
	else:
		response = "Updated_list"
		response += str_tmp

	return response
