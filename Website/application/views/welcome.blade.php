<!DOCTYPE html>
<html>
	<title>&nbsp;</title>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">
     {{ HTML::script('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js'); }}
    <script>
    $(document).ready(function(){
      $(".fancybox").fancybox();
      $('.fancybox-media')
        .attr('rel', 'media-gallery')
        .fancybox({
          openEffect : 'none',
          closeEffect : 'none',
          prevEffect : 'none',
          nextEffect : 'none',

          arrows : false,
          helpers : {
            media : {},
            buttons : {}
          }
        });
    });
    </script>
	</head>
	  <body>

    <div class="site-wrapper">

      <div class="site-wrapper-inner">

        <div class="cover-container">

          <div class="masthead clearfix">
            <div class="inner">
              	<h3 class="masthead-brand">KALAMACOM</h3>
              	<ul class="nav masthead-nav">
             	 <!-- <li class="btn btn-lg btn-info">{{HTML::link('exam/playfriendly/tips',"About Us",array('class'=>'fancybox fancybox.iframe'))}}</li> -->
             	</ul>
            </div>
            <div class="signin">
               {{Form::open('users/adminstration/signin','',array('class'=>'form-signin'))}}
                <!-- <h2 class="form-signin-heading">Please sign in</h2> -->
                @if(!Auth::user())
                <ul class="nav masthead-nav">
                     <input type="email" id="email" name="email" class="form-control" placeholder="Email address" required autofocus>
                  <input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
                  <!-- <label class="checkbox">
                    <input type="checkbox" name="remember-me" value="remember-me"> Remember me
                  </label> -->
                  <button class="btn btn-lg btn-primary btn-block" type="submit" id="submitBtn">Sign In</button>
                </ul>
                @else
                  <p style="margin-top:5px!important;">Welcome <span style="text-transform:uppercase;color:#46b8da;"> {{Auth::user()->firstname}} </span> you are already logged in </p>
                @endif
                
              {{Form::close()}}
              @if(isset($message))
                <div class="errormsg">
                  <span>{{$message}}</span>
                </div>
                @endif
            </div>
          </div>

          <div class="inner cover">
            <h1 class="cover-heading">WELCOME TO KALAMACOM</h1>
            <p class="lead"></p>
            <p class="lead">
              @if(!Auth::user())
                {{HTML::link('users/adminstration/signup','SIGN UP',array('class'=>'btn btn-lg btn-info fancybox fancybox.iframe'))}}
              @else
               {{HTML::link('home/index','Continue .. ',array('class'=>'btn btn-lg btn-info'))}}
              @endif
            </p>
          </div>

          <div class="mastfoot">
            <div class="inner">
            </div>
          </div>

        </div>

      </div>

    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    {{ HTML::style('css/bootstrap.min.css'); }}
    {{ HTML::style('css/cover.css'); }}
    {{ HTML::style('css/style.css'); }}
    {{ HTML::style('css/jquery.fancybox.css') }}
    {{ HTML::script('js/fancybox/source/jquery.fancybox.pack.js?v=2.1.5.js') }}
    {{ HTML::script('js/fancybox/source/helpers/jquery.fancybox-media.js?v=1.0.6.js') }}
  </body>
</html>