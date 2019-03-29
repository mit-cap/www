<?php 
$USERS["jeanyang"] = "jeanyang"; 
$USERS["armando"] = "armando"; 
$USERS["jzim"] = "jzim";
$USERS["justin"] = "justin";
$USERS["admin"] = "";
 
function check_logged(){ 
     global $_SESSION, $USERS; 
     if (!array_key_exists($_SESSION["logged"],$USERS)) { 
          header("Location: login.php"); 
     }; 
}; 
?>
