<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    <title>KALAMACOM</title>
     {{ HTML::style('css/bootstrap.min.css')}}
    {{ HTML::style('//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css')}}
    {{ HTML::style('css/sign_in.css')}}
    {{ HTML::style('css/style.css')}}
     {{ HTML::script('https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js'); }}
    {{ HTML::script('js/jquery-1.10.2.min.js') }}

  <body>

    <div class="container">

      <!-- <form class="form-signin" role="form"> -->
      @if(isset($message))
        {{$message}}
      @endif

    </div> 
     {{ HTML::script('js/bootstrap.min.js') }}
    {{ HTML::script('//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js') }}
    {{ HTML::script('js/effects.js') }}
  </body>
</html>
