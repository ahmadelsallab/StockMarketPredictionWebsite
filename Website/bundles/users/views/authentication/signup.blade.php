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
     {{ HTML::style('css/bootstrap.min.css')}}
    {{ HTML::style('//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css')}}
    {{ HTML::style('css/sign_in.css')}}
    {{ HTML::style('css/style.css')}}
     {{ HTML::script('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js'); }}
    {{ HTML::script('js/jquery-1.10.2.min.js') }}

  <body>

    <div class="container">

      <!-- <form class="form-signin" role="form"> -->
      {{Form::open_for_files('users/adminstration/signup','',array('class'=>'form-signin'))}}
        <h2 class="form-signin-heading">Please sign up</h2>
        <input type="text" name="firstName" class="form-control" placeholder="Your name" required autofocus/>
        <input type="email" name="email" class="form-control" placeholder="Email address" required autofocus>
        <input type="password" name="password" class="form-control" placeholder="Password" required>
        {{Form::hidden('sss','sss')}}
        <div class="upload-btn-container btn-primary btn-block btn">
                {{Form::file('pic',array('class'=>'upload-btn'))}}
          <span>Upload pic</span>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign Up</button>
        @if(isset($message))
                <div class="errormsg">
                  <span>{{$message}}</span>
                </div>
                @endif
      {{Form::close()}}

    </div> 
     {{ HTML::script('js/bootstrap.min.js') }}
    {{ HTML::script('//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js') }}
    {{ HTML::script('js/effects.js') }}
  </body>
</html>
