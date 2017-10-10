function add_new_word_to_history (word, mean){
	/*
	<tr class="word-row">
	 		<th class="word-en">word</th>
	 		<th class="word-vn">mean</th>
	</tr>
	*/
	var table = $('#table-histoty');
	var new_element = 	'<tr class="word-row">' +
	 						'<th class="word-en">' + word + '</th>' +
	 						'<th class="word-vn">' + mean + '</th>' +
						'</tr>';
	table.append(new_element);
}

function change_new_word(word){
	var w = $('#word');
	w.text(word);
}


function first_get_word(){
	en = $('#word').html().trim();
	if (en!="")
		return 0;
	url = '/luyentu/get_word/';
	$.ajax({
		'url': url,
		'type' : 'post',
		'data' : "",
		success : function(response){
			//get new word, change in now-word
			res = JSON.parse(response);
			change_new_word(res.new.en);
		},
		error : function(res){
			alert("error");
			console.log(res);
		}
	});
	$('#input_vi').val("");
}

function filter_words(){
	var checkboxs = $(".checkbox");
	var filter = '';
	for (i in checkboxs){
		if (checkboxs[i].checked){
			var category = checkboxs[i].getAttribute('name');
			filter += category + ";";
		}
	}
	return filter.substring(0, filter.length - 1 );
}

/*
*	
*
*
*/ 
$(document).ready(function(){

	first_get_word();

	$('#submit').on('click', function(){
		url = '/luyentu/get_word/';
		vi = $('#input_vi').val();
		en = $('#word').html();
		json_data = {'en': en, 'vi': vi, 'filter': filter_words()};
		var data = JSON.stringify(json_data);
		$.ajax({
			'url': url,
			'type' : 'post',
			'data' : data,
			success : function(response){
				//get new word, change in now-word, add new word to history
				res = JSON.parse(response);
				console.log(res)
				if (res.old != '')
					add_new_word_to_history(res.old.en, res.old.vi);
				change_new_word(res.new.en);
				$('.history-fd')[0].scrollTop = $('.history-fd')[0].scrollHeight;
			},
			error : function(res){
				alert("error");
				console.log(res);
			}
		});
		$('#input_vi').val("");
		$('#input_en').focus();
		$('#input_en').val("");
	});
});