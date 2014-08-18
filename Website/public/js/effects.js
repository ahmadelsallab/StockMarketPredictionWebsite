$('.navbar-inverse .navbar-nav li a').click(function(){
	$('.active-tab').removeClass('active-tab');
	$(this).addClass('active-tab');
});