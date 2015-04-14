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
				$('#firms').html(data);
			});
		}
	});

});