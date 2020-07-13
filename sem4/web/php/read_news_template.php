<?php

if($num>0){
 
    echo "<table class='table table-hover table-responsive table-bordered'>";
 
    // table headers
    echo "<tr>";
        echo "<th>Text</th>";
        echo "<th>Producer</th>";
        echo "<th>Date</th>";
        echo "<th>Category</th>";
    echo "</tr>";
 
        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)){
        extract($row);
 

        echo "<tr>";
            echo "<td>{$text}</td>";
            echo "<td>{$producer}</td>";
            echo "<td>{$date}</td>";
            echo "<td>{$category}</td>";
    
        echo "</tr>";
        }
 
    echo "</table>";
 
    $page_url="read_news.php?";
    $total_rows = $news->countAll();
 
    // actual paging buttons
    include_once 'paging.php';
}
 
// tell the there are no selfies
else{
    echo "<div class='alert alert-danger'>
        <strong>No news found.</strong>
    </div>";
}
?>