public function action_gettweets(){
			define('CONSUMER_KEY', 'yUAZz1YjQnHWL5ivg6KuXkLjy');
			define('CONSUMER_SECRET', 'oJ0I6MnrnanCBD7JCLT9rmTe2GPvQVmbNDkImEhduhLUuYrhZ4');
			define('ACCESS_TOKEN', '341741972-cPtg3Et0PFi7lcDCTgDYRqJVUKFgkPkmmZIF9aDD');
			define('ACCESS_TOKEN_SECRET', 'kaSldND8zVYJHFRWBlHNvcMwGtn2TptMy3n5gPwt3oROj');
			 
			function search(array $query)
			{
			  $toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
			  return $toa->get('search/tweets', $query);
			}
			$key_words=array("سهم","تداول","سوق","المال","ريال","ارتفع","نقطة","انخفض","ارتفاع","انخفاض","اسهم","أسهم");
			// $key_words=array("سهم","تداول");
			$size=count($key_words);
			$x=Input::get("search_query");
			$y=$x;
			foreach ($key_words as $key => $tag) {
				# code...
				$size--;
				$y=$y." ".$tag;
				if($size !=0)
					$y=$y." OR ".$x." ";
			}
			// $y=$y." &geocode=25,45,3mi ";
			// dd($y);
			$query = array(
			  "q" => $y,
			);
			// $query=$_POST["search_query"];
			$results = search($query);
			$rep_id=Repository::where('title','=',$x)->or_where('title_en','=',$x)->first()->id;
			// dd($results);
			// dd($results);
			// dd(Tweet::where('tweet_id_str','=',$results[0]->id_str)->first());
			foreach ($results->statuses as $key => $result) {
				# code...
				if(Tweet::where('tweet_id_str','=',$result->id_str)->first() == null){
					$tweet=new Tweet();
					$tweet->tweet_id_str=$result->id_str;
					$tweet->content="<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>". $result->text ."</p></div>";
					$tweet->rep_id=$rep_id;
					// $tweet->rep_id;
					$tweet->save();
				}
				// echo $result->content;
			}
				// return Tweet::order_by('id')->get();
			$return_tweets=Tweet::where('rep_id','=',$rep_id)->order_by('id','DESC')->take(10)->get();
				// dd($return_tweets);
				// $i=0;
				foreach ($return_tweets as $result) {
				echo $result->content;
			  // echo $result->user->screen_name . ": " . $result->text . "\n";
				// echo "<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>". $result->text ."</p></div>";
				// echo $i.'<br>';
				// echo $result->id.'<br>';
				// $i++;
					
		}
			  // dd($results);
			// foreach ($results->statuses as $result) {
			//   // echo $result->user->screen_name . ": " . $result->text . "\n";
			// 	echo "<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>". $result->text ."</p></div>";
			// }
	    }