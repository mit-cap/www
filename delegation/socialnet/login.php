<?php 
session_start(); 
include("passwords.php"); 
if ($_POST["ac"]=="log") { /// do after login form is submitted  
  if ($USERS[$_POST["username"]]==$_POST["password"]) { /// check if submittedusername and password exist in $USERS array  
    $_SESSION["logged"]=$_POST["username"]; 
  } else { 
    echo 'Incorrect username/password. Please, try again.'; 
  }; 
};
if (array_key_exists($_SESSION["logged"],$USERS)) { //// check if user is logged or not  
  header( 'Location: index.php' ); 
} else { //// if not logged show login form 
  echo '<h3>Login</h3>';
  echo '<form action="login.php" method="post"><input type="hidden" name="ac" value="log"> '; 
  echo 'Username: <input type="text" name="username" /><br />'; 
  echo 'Password: <input type="password" name="password" /><br />'; 
  echo '<input type="submit" value="Login" />'; 
  echo '</form>'; 
}; 
?>