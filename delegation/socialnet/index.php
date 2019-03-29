<?php 
session_start(); /// initialize session 
include("passwords.php"); 
check_logged(); /// function checks if visitor is logged.  If user is not logged the user is redirected to login.php page  
?>

<html>
<body>

<h3>Search</h3>
<!-- First form that communicates with the server. -->
<form action="search.php" method="post">
<p>
<input type="text" name="searchname" />
<input type="submit" value="Send">
</p>
</form>

<hr>

<h3>Submit Form</h3>

<form action="feedback.php" method="post">
<p>Your Name: <input type="text" name="yourname" /><br />
E-mail: <input type="text" name="email" /></p>

<p>Do you like this website?
<input type="radio" name="likeit" value="Yes" checked="checked" /> Yes
<input type="radio" name="likeit" value="No" /> No
<input type="radio" name="likeit" value="Not sure" /> Not sure</p>

<p>Your comments:<br />
<textarea name="comments" rows="10" cols="40"></textarea></p>

<p><input type="submit" value="Send it!"></p>
</form>

<hr>
<form action="logout.php" method="post">
<input type="submit" value="Logout">
</font>
</body>
</html>
