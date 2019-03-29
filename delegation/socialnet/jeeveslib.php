<?php
include("passwords.php");
// Send an arbitrary string to the backend and get feedback.
function send_jeeves_string ($str) {
  $com = 'python cgi-bin/client.py --sendstr "' . $str . "\"";
  $line = exec($com, $retvals);
  return $retvals;
}

function check_logged(){
     global $_SESSION, $USERS;
     if (!array_key_exists($_SESSION["logged"],$USERS)) {
          header("Location: login.php");
     };
};

// Authenticate a user and a password in a given database.
function password_authenticate($db, $user, $password) {
  return ($USERS[$user]==$password);
}

function quote($str) { return ("\\\"" . $str . "\\\""); }

function set_session_user($user) {
  $_SESSION["logged"] = $user;
}

// To be called once when the session starts.
function connect_to_backend() {
  return send_jeeves_string("connect jconf");
}

function create_table($tablename, $tabletype) {
  return send_jeeves_string("create " . $tablename . " " . $tabletype);
}

function add_to_table($tablename, $fields) {
  return send_jeeves_string("add " . $tablename . " " . $fields);
}

function select_from_table($cols, $tablename) {
  return send_jeeves_string("select " . $cols . " from " . $tablename);
}

function register_user_data($DATA) {
  
  global $_SESSION, $USERS;
  $_SESSION['name'] = $DATA['name'];
  $_SESSION['email'] = $DATA['email'];
  $_SESSION['username'] = $DATA['username'];
  $_SESSION['password'] = $DATA['password'];
  $_SESSION['status'] = $DATA['status'];

  $_SESSION['logged'] = $DATA['username'];
  $_SESSION['init'] = true;

  $status = "0";
  if ($DATA['status'] == "Author") {
    
  } elseif ($DATA['status'] == "Reviewer") {
    $status = "1";
  } elseif ($DATA['status'] == "Editor") {
    $status = "2";
  }

  $fields = array( "0"
    , addslashes(quote($DATA['name']))
    , addslashes(quote($DATA['email']))
    , addslashes(quote($DATA['username']))
    , addslashes(quote($DATA['password']))
    , $status );
  $fieldstr = "[";
  foreach (array_map(quote, $fields) as $field) {
    $fieldstr = $fieldstr . $field . "; ";
  }
  $fieldstr = substr($fieldstr, 0, strlen($fieldstr) - 2);
  $fieldstr = $fieldstr . "]";

  connect_to_backend();
  create_table("users", "user");
  return add_to_table("users", $fieldstr);
}

function check_variables() {
  global $_SESSION;

  $a = session_id();
  if(empty($a)) {
    session_start(); /// initialize session 
  }

  if ($_SESSION['init'] != true) {
    connect_to_backend();
    create_table("users", "user");
  }
}
?>
