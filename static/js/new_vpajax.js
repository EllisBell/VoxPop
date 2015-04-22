$(document).ready(function() {

	$("body").on('click', '.firmBox', function(event) {
		var firm_id;
		firm_id = $(this).attr("data-firmid");
		$.get('/voxpop/show_reviews', {firm_id: firm_id}, function(data) {
			$('#content').html(data);
		});
		$("body").scrollTop(0);
	});

	$("body").on('click', '#nova', function(event) {
		$.get('/voxpop/newreview', function(data) {
			$('#content').html(data);
		});
	});

});