<?php
// core configuration
include_once "../../config/core.php";
 
$require_login=true;
include_once "../login_checker.php";
// include classes
include_once '../../config/database.php';
include_once '../../objects/news.php';
 
// get database connection
$database = new Database();
$db = $database->getConnection();
 
// initialize objects
$news = new News($db);
// set page title
$page_title = "News by date";

// include page header HTML
include_once "../layout_head.php";
$dateS=null;
$dateSt=null;

 $num = -1;
echo "<div class='col-md-12'>";
include_once "date.html";
error_reporting(E_ALL ^ E_NOTICE);  

    $dateS = $_POST['dateStart'];
    $dateSt = $_POST['dateStop'];
      
    $stmt = $news->filter2($dateS,$dateSt,$from_record_num, $records_per_page);
    $num = $stmt->rowCount();
    $page_url="../read_news_date.php?";
 
    // include products table HTML template
    include_once "read_news_template.php";
    echo "</div>";
    
 

?>