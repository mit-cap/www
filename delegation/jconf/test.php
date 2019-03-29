<html>
 <head>
  <title>Social Network</title>
 </head>
 <body>
 <?php echo '<p>Hello World</p>'; ?>
  <?php
echo '<pre>';

// Outputs all the result of shellcommand "ls", and returns
// the last output line into $last_line. Stores the return value
// of the shell command in $retval.
$last_line = system('ls -ld /tmp', $retval);

// Printing additional info
echo '
</pre>
<hr />Last line of the output: ' . $last_line . '
<hr />Return value: ' . $retval .
'Host name: ' . gethostbyname("sketch1");
?>

  <?php $com = 'python bin/client.py'; //"python bin/test_python.py"; //"python bin/run_driver.py";
  $line = exec($com, $retval);
  echo 'output: ' . $line;
  echo 'return: ' . $retval;
  ?>
</html>
