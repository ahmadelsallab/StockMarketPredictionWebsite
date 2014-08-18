<?php
	require_once 'twitteroauth.php';
	class Users_Adminstration_Controller extends Base_Controller{
		 public function action_index($mode=0)
	    {
	        //do our login mechanisms here
	        // echo 'test'; //echo test so we can test this controller out
	        if($mode==0)
	        	return View::make('welcome');
	        else if($mode==1)
	        	return View::make('welcome')
	        	->with();
	    }


	    public function action_signin(){
	    	// dd('test');
	    	if(!$_POST)
	        	// return View::make('users::authentication.signin');
	        	return Redirect::to('home/welcome');
	        else{
		        // dd($credits);
	        	$credits=array('username'=>Input::get('email'),'password'=>Input::get('password'));
		        if(Auth::attempt($credits)){
		        	// dd(Auth::user()->id);
		        	return Redirect::to('home/index');
		        	// return View::make('users::authentication.signin')
		        	// ->with('message','success');
		        	// return('success');
		        }
		        else{
		        	return View::make('welcome')
		        	->with('message','Sorry it seems that your credintials are not right');
		        }
	        }
	        
	    }

	    public function action_signout(){
	    	Auth::logout();
	    	return Redirect::to('/');
	    }

	    public function action_signup(){
	    	if(!$_POST)
	        	return View::make('users::authentication.signup');
	        $firstName=Input::get('firstName');
	        $email=Input::get('email');
	        $password=Input::get('password');
	        // dd("passed");
	        // dd($pic);
	        $newUser=new User();
		        $newUser->firstname=$firstName;
		        $newUser->email=$email;
		        $newUser->password=Hash::make($password);
		        $existedUser = User::where('email','=',Input::get('email'))->first();
				if ($existedUser) return View::make('users::authentication.signup')->with('message','Sorry this mail is already registered');
		        // dd('here');
		        // if()
		    if($newUser->save()){
		    	if(Input::file('pic.name') !=null){

	        		$pic=Input::file('pic');
		    		$picPath='public/uploads/profilepics/';
		       		 $uploadPath='uploads/profilepics/';
			    	$picName='pic_'.$newUser->id;
			    	Input::upload('pic',$picPath,$picName);
			    	$newUser->pic=$uploadPath.$picName;
			    	$newUser->save();
		    	}
	        	return View::make('general_message')
	        	->with('message','Thanks for registration , please login with your new account now .. '.$firstName);
		    }
	        else{
	        	return View::make('users::authentication.signup');
	        }
	    }

	    public function action_tweetmine(){

			define('CONSUMER_KEY', 'yUAZz1YjQnHWL5ivg6KuXkLjy');
			define('CONSUMER_SECRET', 'oJ0I6MnrnanCBD7JCLT9rmTe2GPvQVmbNDkImEhduhLUuYrhZ4');
			define('ACCESS_TOKEN', '341741972-cPtg3Et0PFi7lcDCTgDYRqJVUKFgkPkmmZIF9aDD');
			define('ACCESS_TOKEN_SECRET', 'kaSldND8zVYJHFRWBlHNvcMwGtn2TptMy3n5gPwt3oROj');
			 
			function search(array $query)
			{
			  $toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
			  return $toa->get('search/tweets', $query);
			}
			 // $x=$_POST["search_query"];
			$x="happy";
			$query = array(
			  "q" => $x,
			);
			// $query=$_POST["search_query"];
			$results = search($query);
			  // dd($results);
			foreach ($results->statuses as $result) {
			  // echo $result->user->screen_name . ": " . $result->text . "\n";
				echo "<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>". $result->text ."</p></div>";
			}
	    }
	}
?>