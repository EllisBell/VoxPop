$(document).ready(function() {

	/*$('#suggestion').keyup(function() {
		var query;
		query = $(this).val();
		$.get('/voxpop/suggest_firm/', {suggestion: query}, function(data) {
			$('#firm_search').html(data);
		});
	});*/

	$('#search').keydown(function(event) {
		//var code = event.
		if(event.keyCode == 13) {
			event.preventDefault();
			var query;
			query = $(this).val();
			$.get('/voxpop/firms/', {query: query}, function(data) {
				$('#content').html(data);
			});
		}
	});

	$("body").on('click', '.firmBox', function(event) {
		var firm_id;
		firm_id = $(this).attr("data-firmid");
		$.get('/voxpop/show_reviews', {firm_id: firm_id}, function(data) {
			$('#content').html(data);
		});
		$("body").scrollTop(0);
	});

	$("body").on('mouseover', '.firmBox', function() {
		$(this).css({'background-color' : '#FFCC99', 'opacity' : '1'});
	});

	$("body").on('mouseout', '.firmBox', function() {
		$(this).css({'background-color':'#48D1CC', 'opacity':'0.8'});
	});

	$("body").on('mouseout', '.evenBox', function() {
		$(this).css('background-color', 'gray');
	});

});
