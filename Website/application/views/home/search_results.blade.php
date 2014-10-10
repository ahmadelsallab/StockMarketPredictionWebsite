
	<script>
	var allTime=10;
		$('#repositories li a').click(function(e){
			$('.active').removeClass('active');
			$(this).parent().addClass('active');
	        $search_query=$(this).text();
	        $.ajax({
	            url: '{{URL::to("twitter_mining/mine/gettweets")}}',
	            type: 'POST',
	            data: {search_query:$search_query}
	          }).done(function($result) {
	            $('.tweets-container').html($result);
	            
	          })
	          e.preventDefault()
	          return false;
		});

		// count = 0;
		// 	  var timer = $.timer(
		// 	        function() {
		// 	            count++;
		// 	            console.log(count);
		// 	             if(count==allTime){
		// 	                count=0;
		// 	              $.ajax({
	 //            			url: '{{URL::to("twitter_mining/mine/gettweets")}}',
		// 		            type: 'POST',
		// 		            data: {search_query:$search_query}
		// 		          }).done(function($result) {
		// 		            $('.tweets-container').html($result);
				            
		// 		          });
		// 	             }
		// 	        },
		// 	            6000,
		// 	            true
		// 	          ); 
	</script>
	@foreach ($repositories as $key => $rep)
		<li><a href="#">{{$rep->title}}</a></li>
	@endforeach
