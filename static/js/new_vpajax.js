$(document).ready(function() {

	//TODO include new review text area character countdown (in separate JS file?)

	//search...
	$('#searchbox').keydown(function(event) {
	//var code = event.
		if(event.keyCode == 13) {
			event.preventDefault();
			var query;
			query = $(this).val();
			$.get('/voxpop/newFirms/', {query: query}, function(data) {
				$('#search_results').html(data);
			});
		}
	});

/*	$("body").on('click', '.firmBox', function(event) {
		var firm_id;
		firm_id = $(this).attr("data-firmid");
		$.get('/voxpop/show_reviews', {firm_id: firm_id}, function(data) {
			$('#content').html(data);
		});
		$("body").scrollTop(0);
	});*/

	$("body").on('click', '#nova', function(event) {
		$.get('/voxpop/newreview', function(data) {
			$('#content').html(data);
		});
	});

});