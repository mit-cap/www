<?php 
$a = session_id();
if(empty($a)) session_start(); /// initialize session 
include("jeeveslib.php");
check_logged(); /// function checks if visitor is logged.  If user is not logged the user is redirected to login.php page  
?> 

<html>
<body>
<h3>Your Feedback Summary</h3>

Your name is: <?php echo $_POST['yourname']; ?><br />
Your e-mail: <?php echo $_POST['email']; ?><br />
<br />

Do you like this website? <?php echo $_POST['likeit']; ?><br />
<br />

Comments:<br />
<?php
  echo $_POST['comments'];
?>
<hr>
<!--- Display feedback from Jeeves server. -->
<h3>Feedback from Server</h3>
<?php
  $retvals = send_jeeves_string($_POST['comments']);
  foreach ($retvals as $retval) {
    echo $retval . '<br>';
  }
  echo '<br>';
?>

</body>
</html>
