<?php
// require_once 'twitteroauth.php';
 
// define('CONSUMER_KEY', 'yUAZz1YjQnHWL5ivg6KuXkLjy');
// define('CONSUMER_SECRET', 'oJ0I6MnrnanCBD7JCLT9rmTe2GPvQVmbNDkImEhduhLUuYrhZ4');
// define('ACCESS_TOKEN', '341741972-cPtg3Et0PFi7lcDCTgDYRqJVUKFgkPkmmZIF9aDD');
// define('ACCESS_TOKEN_SECRET', 'kaSldND8zVYJHFRWBlHNvcMwGtn2TptMy3n5gPwt3oROj');
 
// function search(array $query)
// {
//   $toa = new TwitterOAuth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET);
//   return $toa->get('search/tweets', $query);
// }
//  $x=$_POST["search_query"];
// $query = array(
//   "q" => $x,
// );
// // $query=$_POST["search_query"];
// $results = search($query);
  
// foreach ($results->statuses as $result) {
//   // echo $result->user->screen_name . ": " . $result->text . "\n";
// 	echo "<div class='testing col-md-12 row'><img class='twitter-prof-pic' src='".$result->user->profile_image_url."'/>" . "		" ."<p class='twitter-tweet-content'>". $result->text ."</p></div>";
// }

$dbhost = '127.0.0.1:3036';
$dbuser = 'admin';
$dbpass = '';
// $dbname="kalamakom";
$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
$sql = 'INSERT INTO tweets '.
       '(id,rep_id, content) '.
       'VALUES ( "1", "1", "Test" )';

mysql_select_db('kalamacom');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not enter data: ' . mysql_error());
}
echo "Entered data successfully\n";
mysql_close($conn);
?>