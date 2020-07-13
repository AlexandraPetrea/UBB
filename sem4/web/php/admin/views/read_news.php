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
$page_title = "News";

// include page header HTML
include_once "../layout_head.php";

echo "<div class='col-md-12'>";

      
    $stmt = $news->readAll($from_record_num, $records_per_page);
    $num = $stmt->rowCount();
    $page_url="read_news.php?";
 
    // include products table HTML template
    include_once "read_news_template.php";
    echo "</div>";
    
 

?>