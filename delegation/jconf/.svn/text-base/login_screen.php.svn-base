<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<META name="verify-v1" content="E7CAKdK/YXZzYIZ/7WWURP/gYAyHqrf6YOcW8U1AjaM=" />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<title>jconf - home</title>
<meta name="" content="" />
<link href="default.css" rel="stylesheet" type="text/css" />
</head>
<body>
<div id="wrapper">
  <div id="header">
  <h1>jconf . csail</h1>
  </div>
  <div id="menu">
    <ul>
      <li><a href="signup.php" accesskey="7" title="">Sign Up</a></li>
    </ul>
  </div>
  <div id="content">
  <?php
    if ($_POST["ac"]=="log") { /// do after login form is submitted  
      echo 'Incorrect username/password. Please, try again.';
      echo '';
    };
  ?>

    <?php print_r($USERS); ?>
    <form action="login.php" method="post">
    <input type="hidden" name="ac" value="log">
    Username: <input type="text" name="username" /><br />
    Password: <input type="password" name="password" /><br />
    <input type="submit" class="button" value="Login" />
    </form>
  </div>
  <div id="footer">
    <p>&copy; 2011 Jean Yang.</p>
  </div>
</div>
</body>
</html>
