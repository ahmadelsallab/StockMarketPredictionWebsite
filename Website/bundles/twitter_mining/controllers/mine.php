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
		// dd();
		$repositories=Repository::all();
		define('CONSUMER_KEY', 'yUAZz1YjQnHWL5ivg6KuXkLjy');
		define('CONSUMER_SECRET', 'oJ0I6MnrnanCBD7JCLT9rmTe2GPvQVmbNDkImEhduhLUuYrhZ4');
		define('ACCESS_TOKEN', '341741972-cPtg3Et0PFi7lcDCTgDYRqJVUKFgkPkmmZIF9aDD');
		define('ACCESS_TOKEN_SECRET', 'kaSldND8zVYJHFRWBlHNvcMwGtn2TptMy3n5gPwt3oROj');
			 
		function search(array $query)
		{
		  $toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
		  return( $toa->get('search/tweets', $query));
		}
		$key_words="(سهم OR اسهم OR أسهم OR نقطة OR تداول OR مال  OR ارتفع OR ارتفاع OR انخفض OR انخفاض)‎";
		
		if($stock_name==null){
			$x=Input::get("search_query");
			$y="";
			$rep=Repository::where('title','=',$x)->or_where('title_en','=',$x)->first();
			$used_name_ar=$rep->used_name_ar;
			$used_name_en=$rep->used_name_en;
			$y=$y."((".'"'.$used_name_en.'"'.")"." OR "."(".'"'.$used_name_ar.'"'."))"." AND ".$key_words ;
			$query = array(
			 "q" => $y,
			);
			//$path_py=path('sys');
			//$path_py= str_replace('\kalamakom-alpha2\laravel','', $path_py).'kalam';
			$path_py = '/srv/www/htdocs/kalam';
			// $path_py="";
			if($rep->title_en=="Tassi"){
					$path_py=$path_py.'/test_filter_class_tassi.py'.' 2>&1';
					// dd($path_py);
				}
				else{
					// dd("there");
					$path_py=$path_py.'/test_filter_class_general.py'.' 2>&1';
				}
			$results = search($query);
			$rep_id=$rep->id;
			$size=sizeof($results->statuses)-1;
			$res=array();
			for($i=0;$i<sizeof($results->statuses);$i++){
				$res[$i]=$results->statuses[$size-$i];
			}
			$tst=array();
			// array_push($tst, "السلام عليكم إغلاق 8704 الإإيجابية بالحفاظ على 8700 تجاوز 8715 -8718 سيتجه الى 8749 عدم التجاوز الهبوط 8658 كسرها 8575");
			foreach ($res as $key => $value) {
				# code...
				// array_push($tst,$value->text."\r\n");
				array_push($tst,$value->text);
				// $tst[$key]=$value->text."\r\n";
			}
			// dd($tst);
			// dd($tst[5]);
			// dd($tst);
			// $tst2=array();
			// array_push($tst2, "#توصيات #الاسهم #تداول #تاسي #tasi #tadawul #saudi ليل: سهم قادم ماليآ حلواني  =  سدافكو:  http://t.co/As2WWMcTzq"."\r\n");
			// array_push($tst2, "أرباح 3 صناديق جكومية 21 مليار هذا من إستثماراتهم المعلنة فقط. والناس تضارب في شركات خاسره #تاسي #توصيات http://t.co/DycgSsvbsD"."\r\n");
			// array_push($tst2, "أسلاك 40 هو الاخر يبدوا جاهز بمحافظته على 39 نراقب 41.30 ثم 43.80 ليتحرر بعدها #تداول #تاسي"."\r\n");
			// array_push($tst2, "#توصيات #الاسهم #تداول #تاسي #tasi #tadawul #saudi مسيرة سهم: مسيرة السوق السعودي وكما رسمت بالملي وشارتات مه... http://t.co/45HyCrwSfn"."\r\n");
			// array_push($tst2,"السلام عليكم إغلاق 8704 الإإيجابية بالحفاظ على 8700 تجاوز 8715 -8718 سيتجه الى 8749 عدم التجاوز الهبوط 8658 كسرها 8575"."\r\n");
			// array_push($tst2,"@fahad2120 اتوقع قريب تتحرك السهم محصور بين 30 و34 التحرر من المقاومه سيعطي بسخاء والله اعلم فقط باجتيازها #تاسي #انعام"."\r\n");
			// array_push($tst2, "RT @Osama_Alssudmi: تبوك الزراعيه الآن عند دعم 34 الحفاظ سيتجه الى 34.60  #تاسي #تداول"."\r\n");
			// array_push($tst2, "RT @Osama_Alssudmi: المؤشر وصل نقطة المقاومه 8898 تجاوزها يستهدف 8908 لحظيا #تاسي #تداول"."\r\n");
			// array_push($tst2, "المؤشر وصل نقطة المقاومه 8898 تجاوزها يستهدف 8908 لحظيا #تاسي #تداول"."\r\n");
			// dd()
			// $myfile = fopen("xtest.txt", "w")
			// dd($tst2);


			//Working set
			// file_put_contents("D:\xtest.txt",$tst);
			// $tres=exec($path_py,$tres);
			// $tres_d = json_decode($tres, true);
			// foreach ($tres_d as $key => $value) {
			// 	# code...
			// 	echo($value);
			// }
			// dd("tst");
			//end of workking

			//new
			$xml = new DOMDocument("1.0");
			$root = $xml->createElement("tweets");
			$xml->appendChild($root);
			foreach ($tst as $key => $value) {
				# code...

				

				$tweet = $xml->createElement("tweet");
				$root->appendChild($tweet);

				$titleText = $xml->createTextNode("'".$value."'");
				$tweet->appendChild($titleText);
			}
			$xml->formatOutput = true;
			// echo "<xmp>". $xml->saveXML() ."</xmp>";
			//$xml->save("/srv/www/htdocs/kalam/Website/xtest.txt.xml") or die("Error");
			$xml->save("xtest.txt.xml") or die("Error");
			// dd("Stop Exec");
			$tres=exec('/opt/ActivePython-3.3/bin/python3 '.$path_py,$tres);
			$tres_d = json_decode($tres, true);
			// dd($tres_d);
			//end new 
			foreach ($res as $key => $result) {
				# code...
				// dd($path_py);
				// $tres=exec($path_py. escapeshellarg(json_encode($result->text)).' 2>&1',$tres);
				// dd($tres);
				// $tres_d = json_decode($tres, true);
				// echo("ssssssss".$tres_d[0]);
				// echo($tres_d[0]);
				// echo($tres_d[$key]);
				// dd($res);
				if(Tweet::where('tweet_id_str','=',$result->id_str)->first() == null && $tres_d[$key]==1){
					// dd("ym here");
					// echo("um here");
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