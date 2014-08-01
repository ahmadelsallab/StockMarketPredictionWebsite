
	<script>
	var allTime=10;
		$('#repositories li a').click(function(e){
			$('.active').removeClass('active');
			$(this).parent().addClass('active');
	        $search_query=$(this).text();
	        // console.log($search_query);
	        // console.log("ssss");
	        $.ajax({
	            // url: '{{URL::to("home/search")}}',
	            // url: '../../twitteroauth/twitter.php',
	            url: '{{URL::to("twitter_mining/mine/gettweets")}}',
	            type: 'POST',
	            data: {search_query:$search_query}
	          }).done(function($result) {
	            $('.tweets-container').html($result);
	            
	          })
	          e.preventDefault()
	          return false;
		});

		count = 0;
			  var timer = $.timer(
			        function() {
			            count++;
			            console.log(count);
			             // $('.timer .time').html(allTime-count);
			             if(count==allTime){
			                count=0;
			              $.ajax({
				            // url: '{{URL::to("home/search")}}',
	            url: '{{URL::to("twitter_mining/mine/gettweets")}}',
				            // url: '../../twitteroauth/twitter.php',
				            type: 'POST',
				            data: {search_query:$search_query}
				          }).done(function($result) {
				            $('.tweets-container').html($result);
				            
				          });
			             }
			        },
			            6000,
			            true
			          );  

		// $("#tst").click(function(e){
	 //        // $search_query=$("#search_query").val();
	 //        // console.log("SSSS");
	 //        $search_query="sad";
	 //      // $.ajax({url:"demo_test.txt",success:function(result){
	 //        // $("#div1").html(result);
	 //      // }});
	 //        $.ajax({
	 //            // url: '{{URL::to("home/search")}}',
	 //            url: '../../twitteroauth/twitter.php',
	 //            type: 'POST',
	 //            data: {search_query:$search_query}
	 //          }).done(function($result) {
	 //            $('.main').html($result);
	            
	 //          })
	 //          e.preventDefault()
	 //          return false;
	 //    });
	</script>
	@foreach ($repositories as $key => $rep)
		<li><a href="#">{{$rep->title}}</a></li>
	@endforeach
