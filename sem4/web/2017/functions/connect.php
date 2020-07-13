<?php
  function connect() {
    try {
      $con = new PDO("mysql:host=localhost;charset=utf8mb4", "root", ""));
      $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    } catch (PDOExceptinon $pikatchu) {
      echo "Error connecting to database " . $pikachu->getMessage();
    }
    /// database exam
    $con->query("USE exam");
        try {
      $sql = "CREATE TABLE IF NOT EXISTS chat (
        user_id INT PRIMARY KEY AUTO_INCREMENT,
        user VARCHAR(255) NOT NULL,
        secretQuestion VARCHAR(1024) NOT NULL,
        secretAnswer VARCHAR(1024) NOT NULL
      )";
      $con->query($sql);
    } catch (PDOException $pikachu) {
      //echo $sql . "<br>" . $pikachu->getMessage();
    }
    return $con;
  }
?>