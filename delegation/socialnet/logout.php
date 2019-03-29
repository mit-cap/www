<?php
session_start();
include 'passwords.php';
check_logged();
session_unset();
session_destroy();
echo 'You are logged out.<br>';
echo '<a href="login.php">Log in</a>';
?>
