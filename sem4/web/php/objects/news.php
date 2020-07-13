<?php
// 'news' object
class News{
 
    // database connection and table name
    private $conn;
    private $table_name = "news";
 
    // object properties
    public $id;
    public $text;
    public $producer;
    public $date;
    public $category;
 
    // constructor
    public function __construct($db){
        $this->conn = $db;
    }

function create(){
 
    // to get time stamp for 'created' field
    $this->date=date('Y-m-d H:i:s');
 
    // insert query
    $query = "INSERT INTO
                " . $this->table_name . "
            SET
                text = :text,
                producer = :producer,
                date = :date,
                category = :category";
 
    // prepare the query
    $stmt = $this->conn->prepare($query);
 
    // sanitize
    $this->text=htmlspecialchars(strip_tags($this->text));
    $this->producer=htmlspecialchars(strip_tags($this->producer));
    $this->category=htmlspecialchars(strip_tags($this->category));
 
    // bind the values
    $stmt->bindParam(':text', $this->text);
    $stmt->bindParam(':producer', $this->producer);
    $stmt->bindParam(':date', $this->date);
    $stmt->bindParam(':category', $this->category);
    
 
    // execute the query, also check if query was successful
    if($stmt->execute()){
        return true;
    }else{
        $this->showError($stmt);
        return false;
    }
 
    }

function textExists(){
 
    $query = "SELECT id,text,producer,date,category
            FROM " . $this->table_name . "
            WHERE text = ?
            LIMIT 0,1";
 
    // prepare the query
    $stmt = $this->conn->prepare( $query );
 
    // sanitize
    $this->text=htmlspecialchars(strip_tags($this->text));
 
    // bind given email value
    $stmt->bindParam(1, $this->text);
 
    // execute the query
    $stmt->execute();
 
    // get number of rows
    $num = $stmt->rowCount();
 
    // if email exists, assign values to object properties for easy access and use for php sessions
    if($num>0){
 
        // get record details / values
        $row = $stmt->fetch(PDO::FETCH_ASSOC);
 
        // assign values to object properties
        $this->id = $row['id'];
        $this->producer = $row['producer'];
        $this->date = $row['date'];
        $this->category = $row['category'];

 
        // return true because email exists in the database
        return true;
    }
 
    // return false if email does not exist in the database
    return false;
}

function update(){
 
    // to get time stamp for 'created' field
    $this->date=date('Y-m-d H:i:s');
 
    // insert query
    $query = "UPDATE
                " . $this->table_name . "
            SET
                producer = :producer,
                date = :date,
                category = :category
                WHERE text=:text";
 
    // prepare the query
    $stmt = $this->conn->prepare($query);
   
    // sanitize
    $this->text=htmlspecialchars(strip_tags($this->text));
    $this->producer=htmlspecialchars(strip_tags($this->producer));
    $this->category=htmlspecialchars(strip_tags($this->category));
 
    // bind the values
    $stmt->bindParam(':producer', $this->producer);
    $stmt->bindParam(':date', $this->date);
    $stmt->bindParam(':category', $this->category);
    $stmt->bindParam(':text', $this->text);
    
    
    // execute the query, also check if query was successful
    if($stmt->execute()){
        return true;
    }else{
        $this->showError($stmt);
        return false;
    }
 
    }
    // read all user records
function readAll($from_record_num, $records_per_page){
 
    // query to read all user records, with limit clause for pagination
    $query = "SELECT
                id,
                text,
                producer,
                date,
                category
            FROM " . $this->table_name . "
            ORDER BY id DESC
            LIMIT ?, ?";
 
    // prepare query statement
    $stmt = $this->conn->prepare( $query );
 
    // bind limit clause variables
    $stmt->bindParam(1, $from_record_num, PDO::PARAM_INT);
    $stmt->bindParam(2, $records_per_page, PDO::PARAM_INT);
 
    // execute query
    $stmt->execute();
 
    // return values
    return $stmt;
}
function filter($category, $from_record_num, $records_per_page){
 
    // query to read all user records, with limit clause for pagination
    $query = "SELECT
                id,
                text,
                producer,
                date,
                category
            FROM " . $this->table_name . "
            WHERE category = ?
            ORDER BY id DESC
            LIMIT ?, ?";
 
    // prepare query statement
    $stmt = $this->conn->prepare( $query );
 
    // bind limit clause variables
    $stmt->bindParam(1, $category, PDO::PARAM_STR);
    $stmt->bindParam(2, $from_record_num, PDO::PARAM_INT);
    $stmt->bindParam(3, $records_per_page, PDO::PARAM_INT);
 
    // execute query
    $stmt->execute();
 
    // return values
    return $stmt;
}
function filter2($dateStart,$dateStop, $from_record_num, $records_per_page){
 
    // query to read all user records, with limit clause for pagination
    $query = "SELECT
                id,
                text,
                producer,
                date,
                category
            FROM " . $this->table_name . "
            WHERE date BETWEEN ? AND ?
            ORDER BY id DESC
            LIMIT ?, ?";
 
    // prepare query statement
    $stmt = $this->conn->prepare( $query );
 
    // bind limit clause variables
    $stmt->bindParam(1, $dateStart);
    $stmt->bindParam(2, $dateStop);
    $stmt->bindParam(3, $from_record_num, PDO::PARAM_INT);
    $stmt->bindParam(4, $records_per_page, PDO::PARAM_INT);
 
    // execute query
    $stmt->execute();
 
    // return values
    return $stmt;
}
public function countAll(){
 
    // query to select all user records
    $query = "SELECT id FROM " . $this->table_name . "";
 
    // prepare query statement
    $stmt = $this->conn->prepare($query);
 
    // execute query
    $stmt->execute();
 
    // get number of rows
    $num = $stmt->rowCount();
 
    // return row count
    return $num;
}
}