<?php 
$a = session_id();
if(empty($a)) session_start(); /// initialize session 
include("passwords.php"); 
check_logged(); /// function checks if visitor is logged.  If user is not logged the user is redirected to login.php page  
?> 

<html>
<body>
<h3>Search</h3><br />
<?php
  echo 'You searched for ' . $_POST['searchname'] . '.';
?>
<hr>
<h3>Feedback from Server</h3>
<?php
  $sendstr = (string)$_POST['searchname'];
  $com = 'python cgi-bin/client.py --sendstr ' . $sendstr;
$line = exec($com, $retvals);
  foreach ($retvals as $retval) {
    echo $retval . '<br>';
  }
  echo '<br>';
  echo $sendstr;
?>

</body>
</html>
