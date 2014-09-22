<?php
require_once 'twitteroauth.php';
class Twitter_Mining_Mine_Controller extends Base_Controller {

	/*
	|--------------------------------------------------------------------------
	| The Default Controller
	|--------------------------------------------------------------------------
	|
	| Instead of using RESTful routes and anonymous functions, you might wish
	| to use controllers to organize your application API. You'll love them.
	|
	| This controller responds to URIs beginning with "home", and it also
	| serves as the default controller for the application, meaning it
	| handles requests to the root of the application.
	|
	| You can respond to GET requests to "/home/profile" like so:
	|
	|		public function action_profile()
	|		{
	|			return "This is your profile!";
	|		}
	|
	| Any extra segments are passed to the method as parameters:
	|
	|		public function action_profile($id)
	|		{
	|			return "This is the profile for user {$id}.";
	|		}
	|
	*/

	public function action_index(){
	
		return View::make('home.index');
	}

	public function action_search(){
		$search_query=Input::get('search_query');
        $repositories=Repository::where('title','like','%'.$search_query.'%')->or_where('title_en','like','%'.$search_query.'%')->get();
       		return View::make('home.search_results')
			->with('repositories',$repositories);
	}

	public function action_gettweets($stock_name=null){
		$repositories=Repository::all();
		define('CONSUMER_KEY', 'yUAZz1YjQnHWL5ivg6KuXkLjy');
		define('CONSUMER_SECRET', 'oJ0I6MnrnanCBD7JCLT9rmTe2GPvQVmbNDkImEhduhLUuYrhZ4');
		define('ACCESS_TOKEN', '341741972-cPtg3Et0PFi7lcDCTgDYRqJVUKFgkPkmmZIF9aDD');
		define('ACCESS_TOKEN_SECRET', 'kaSldND8zVYJHFRWBlHNvcMwGtn2TptMy3n5gPwt3oROj');
			 
		function search(array $query)
		{
		  $toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
		  // dd( $toa->get('search/tweets', $query));
		  return( $toa->get('search/tweets', $query));
		}
		// $key_words=array("سهم","تداول","سوق","المال","ريال","ارتفع","نقطة","انخفض","ارتفاع","انخفاض","اسهم","أسهم");
		$key_words="(سهم OR اسهم OR أسهم OR نقطة OR تداول OR مال  OR ارتفع OR ارتفاع OR انخفض OR انخفاض)‎";
		// $size=count($key_words);
		
		if($stock_name==null){
			$x=Input::get("search_query");
			$y="";
			$rep=Repository::where('title','=',$x)->or_where('title_en','=',$x)->first();
			$used_name_ar=$rep->used_name_ar;
			$used_name_en=$rep->used_name_en;
			$y=$y."((".$used_name_en.")"." OR "."(".$used_name_ar."))"." AND ".$key_words ;
			// dd($y);
			// $syn_ar=$rep->syn_ar;
			// $syn_array_ar=explode("-",$syn_ar);
			// $syn_array_en=explode("-",$syn_en);
			// $syn_queries_ar=array();
			// $syn_queries_en=array();
			// for($i=0;$i<sizeof($syn_array_ar);$i++){
			// 	array_push($syn_queries,$syn_array_ar[$i]);
			// 	$y=$y.$syn_array_ar[$i]." OR ";
			// }
			// $y=$y.$x;
			// foreach ($key_words as $key => $tag) {
			// 	# code...
			// 	$size--;
			// 	$y=$y." ".$tag;
			// 	if($size !=0){
			// 		$y=$y." OR ".$x." ";
			// 	}
			// }
			$query = array(
			 "q" => $y,
			 // "geocode"=>"24.0,45.0,100mi"
			);
			// dd($query["q"]);
			$results = search($query);
			// dd($results);
			$rep_id=$rep->id;
			$size=sizeof($results->statuses)-1;
			$res=array();
			for($i=0;$i<sizeof($results->statuses);$i++){
				$res[$i]=$results->statuses[$size-$i];
			}
			foreach ($res as $key => $result) {
				# code...
				if(Tweet::where('tweet_id_str','=',$result->id_str)->first() == null){
					$tweet=new Tweet();
					$tweet->tweet_id_str=$result->id_str;
					$tweet->content="<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>".$result->text ."</br><span>".$result->created_at."</span></br><span class='blue-color'>المُتابعين : ".$result->user->followers_count."</span></p></div>";
					$tweet->rep_id=$rep_id;
					$tweet->save();
				}
			}
			$return_tweets=Tweet::where('rep_id','=',$rep_id)->order_by('id','DESC')->take(10)->get();
			foreach ($return_tweets as $result) {
				echo $result->content;
					
			}
	    }
	    else{
	    	$x=$stock_name;
			$y=$x;
			foreach ($key_words as $key => $tag) {
				# code...
				$size--;
				$y=$y." ".$tag;
				if($size !=0)
					$y=$y." OR ".$x." ";
			}
			$query = array(
			  "q" => $y,
			);
			$results = search($query);
			// dd($results);
			$rep_id=Repository::where('title','=',$x)->or_where('title_en','=',$x)->first()->id;
			$size=sizeof($results->statuses)-1;
			$res=array();
			for($i=0;$i<sizeof($results->statuses);$i++){
				$res[$i]=$results->statuses[$size-$i];
			}
			foreach ($res as $key => $result) {
				# code...
				if(Tweet::where('tweet_id_str','=',$result->id_str)->first() == null){
					$tweet=new Tweet();
					$tweet->tweet_id_str=$result->id_str;
					$tweet->content="<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>".$result->text ."</br><span>".$result->created_at."</span></br><span class='blue-color'>المُتابعين : ".$result->user->followers_count."</span></p></div>";
					$tweet->rep_id=$rep_id;
					$tweet->save();
				}
			}
			$return_tweets=Tweet::where('rep_id','=',$rep_id)->order_by('id','DESC')->take(10)->get();
			// dd($return_tweets);
			return View::make("home.index")
			->with("return_tweets",$return_tweets)
			->with("repositories",$repositories);
	    }
	}
}