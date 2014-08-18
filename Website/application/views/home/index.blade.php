<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <title>KALAMAKOM</title>

    <!-- Bootstrap core CSS -->
    {{ HTML::style('css/bootstrap.min.css')}}
    {{ HTML::style('//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css')}}
    <!-- Custom styles for this template -->
    {{ HTML::style('css/dashboard.css')}}
    {{ HTML::style('css/style.css')}}
    {{ HTML::style('fonts/fontin/stylesheet.css')}}
     {{ HTML::script('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js'); }}
    {{ HTML::script('js/jquery-1.10.2.min.js') }}
    {{ HTML::script('js/jquery-1.10.2.min.js') }}

  <style type="text/css">
          body{
        font-family: 'fontinregular';
              }
    </style>
	@if(Config::get('application.language')==='ar')
    	{{ HTML::style('css/style_ar.css')}}
    @endif
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">{{__('main_components.kalamakom')->get()}}</a>
        </div>
        <div class="navbar-collapse collapse">
          <ul class="nav navbar-nav header-nav">
            <li><a href="#" class="active-tab">{{__('main_components.home')->get()}}</a></li>
            <li><a href="#">{{__('main_components.about')->get()}}</a></li>
            <li><a href="#">{{__('main_components.contactus')->get()}}</a></li>
          </ul>
          <ul id="changeLanguage" class="nav navbar-nav language-bar">
              <li> <a href="" class="profile-link">{{Html::image(Auth::user()->pic,'',array('class'=>'header-avatar'))}}</a></li>
              <li class="header-user-name"> {{Auth::user()->firstname}} </li>
            <li>{{HTML::link('#','Settings',array('id'=>'settings', 'class'=>'settings-btn'))}}</li>
            <li>{{HTML::link('language/en/','EN',array('id'=>'EN', 'class'=>'header-btn btn btn-default active-lang'))}}</li>
            <li>{{HTML::link('language/ar/','عربى',array('id'=>'AR','class'=>'header-btn btn btn-default'))}}</li>
             @if(Auth::user())
              <li>{{HTML::link('users/adminstration/signout','Sign Out',array('id'=>'EN', 'class'=>'header-btn btn btn-default'))}}</li>
            @endif
          </ul>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
        	<form class="navbar-form">
		        	<input id="search_query" type="text" class="form-control" placeholder="{{__('main_components.search')->get()}} ..." name="search_query">
		        </form>
          <ul class="nav nav-sidebar" id="repositories">
            @foreach ($repositories as $key => $rep)
              <li><a href="#">{{$rep->title}}</a></li>
            @endforeach
          </ul>
          
        </div>
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
          <h1 class="page-header">{{__('main_components.tweets')->get()}}</h1>
          <div class="tweets-container"></div>
          {{Form::open()}}
           <!--  <a href="../../twitteroauth/twitter.php">test</a>
            <a id="tst" href="#">test ajax tweets</div> -->
          {{Form::close()}}
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script>
    $(document).ready(function(){
    	$("#search_query").keyup(function(e){
    		$search_query=$("#search_query").val();
		  // $.ajax({url:"demo_test.txt",success:function(result){
		    // $("#div1").html(result);
		  // }});
		  	$.ajax({
					  url: '{{URL::to("home/search")}}',
					  type: 'POST',
					  data: {search_query:$search_query}
					}).done(function($repositories) {
					  $('#repositories').html($repositories);
					  
					})
					e.preventDefault()
					return false;
		});
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
		$("#tst").click(function(e){
        // $search_query=$("#search_query").val();
        // console.log("SSSS");
        $search_query="sad";
      // $.ajax({url:"demo_test.txt",success:function(result){
        // $("#div1").html(result);
      // }});
        $.ajax({
            // url: '{{URL::to("home/search")}}',
            url: '../../twitteroauth/twitter.php',
            type: 'POST',
            data: {search_query:$search_query}
          }).done(function($result) {
            $('.main').html($result);
            
          })
          e.preventDefault()
          return false;
    });
    
    });
    	
    </script>
    {{ HTML::script('js/bootstrap.min.js') }}
    {{ HTML::script('//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js') }}
    {{ HTML::script('js/jquery.timer.js'); }}
    {{ HTML::script('js/effects.js') }}
  </body>
</html>
