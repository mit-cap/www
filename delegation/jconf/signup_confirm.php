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
    </ul>
  </div>
  <div id="content">
    <h3>Confirmation</h3>
    <p>Please confirm your information.</p>
    <p>
    <table>
    <tr><td>Name</td><td><?php echo $_POST['yourname']; ?></td></tr>
    <tr><td>E-mail</td><td><?php echo $_POST['email']; ?></td></tr>
    <tr><td>Username</td><td><?php echo $_POST['username'] ?></td></tr>
    <tr><td>Password</td><td><?php echo $_POST['password'] ?></td></tr>
    <tr><td>Status</td><td><?php echo $_POST['status'] ?></td></tr>
    </table>
    </p>
    <form action="index.php" method="post">
    <input type="hidden" name="log" value="record">
    <input type="hidden" name="yourname" value=<?php echo $_POST['yourname']?>>
    <input type="hidden" name="email" value=<?php echo $_POST['email']?>>
    <input type="hidden" name="username" value=<?php echo $_POST['username']?>>
    <input type="hidden" name="password" value=<?php echo $_POST['password']?>>
    <input type="hidden" name="status" value=<?php echo $_POST['status']?>>
    <input type="submit" class="button" value="Confirm" />
    </form>
  </div>
  <div id="footer">
    <p>&copy; 2011 Jean Yang.</p>
  </div>
</div>
</body>
</html>

