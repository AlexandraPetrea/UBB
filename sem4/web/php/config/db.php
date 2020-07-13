<?php

$host = "127.0.0.1";
$db_name = "loginsystem";
$username = "root";
$password = "";
$conn = mysqli_connect($host,$username,$password,$db_name);
 
    if(!$conn){
        die("Connection failed!." . mysqli_connect_error());
    }
?>