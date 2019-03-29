<?php 
include("jeeveslib.php");
include("initdb.php");

check_variables();
?>

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<META name="verify-v1" content="E7CAKdK/YXZzYIZ/7WWURP/gYAyHqrf6YOcW8U1AjaM=" />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>jconf - home</title>
<meta name="Jean Yang is a graduate student at MIT CSAIL." content="" />
<link href="default.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="wrapper">
  <div id="header">
  <h1>jconf . csail</h1>
  </div>
  <div id="menu">
    <ul>
      <li class="active"><a href="index.php" accesskey="1" title="">Home</a></li>
      <li><a href="submissions.php" accesskey="3" title="">Submissions</a></li>
      <li><a href="reviews" accesskey="4" title="">Reviews</a></li>
      <li><a href="logout.php" accesskey="7" title="">Logout</a></li>
    </ul>
  </div>
  <div id="content">
<?php
if ($_POST['log']=="record") {
  $DATA['name'] = $_POST['yourname'];
  $DATA['email'] = $_POST['email'];
  $DATA['username'] = $_POST['username'];
  $DATA['password'] = $_POST['password'];
  $DATA['status'] = $_POST['status'];
  $result = register_user_data($DATA);
  foreach ($result as $r) {
    echo $r;
  }
}
?>
  <p><b>Welcome</b> <?php echo $_SESSION['name']; ?>!  You are a(n) <?php echo $_SESSION['status']?>.<br>
    (<?php echo $_SESSION['email']?>)</p>
    <p>
<?php
$lines = select_from_table("[name]", "users");
foreach ($lines as $line) {
  echo $line;
}
?>
    </p>
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
  </div>
  <div id="footer">
    <p>&copy; 2011 Jean Yang.</p>
  </div>
</div>
</body>
</html>
