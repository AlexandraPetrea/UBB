<?php
// core configuration
include_once "../../config/core.php";
 
// set page title
$page_title = "Update the news";
 

//include_once "login_checker.php";
 
// include classes
include_once '../../config/database.php';
include_once '../../objects/news.php';
include_once "../../libs/php/utils.php";
 
// include page header HTML
include_once "../layout_head.php";
 
echo "<div class='col-md-12'>";
 
    // if form was posted
if($_POST){
 
    // get database connection
    $database = new Database();
    $db = $database->getConnection();
 
    // initialize objects
    $news = new News($db);
    $utils = new Utils();
    $news->text=$_POST['text'];
    if(!$news->textExists()){
        echo "<div class='alert alert-danger'>";
            echo "The text you specified is not registered. Please try again or <a href='{$home_url}/admin/add.php'>go adding news.</a>";
        echo "</div>";
    }
 
    else{
        // set values to object properties
$news->producer=$_POST['producer'];
$news->date=$_POST['date'];
$news->category=$_POST['category'];

// create the user
if($news->update()){
 
    echo "<div class='alert alert-info'>";
        echo "Successfully added. <a href='{$home_url}login'>Please login</a>.";
    echo "</div>";
 
    // empty posted values
    $_POST=array();
 
}else{
    echo "<div class='alert alert-danger' role='alert'>Unable to update. Please try again.</div>";
}
}
    
}
?>
<form action='update.php' method='post' id='update'>
 
    <table class='table table-responsive'>
 
        <tr>
            <td class='width-30-percent'>Text</td>
            <td><input type='textarea' name='text' class='form-control' required value="<?php echo isset($_POST['text']) ? htmlspecialchars($_POST['text'], ENT_QUOTES) : "";  ?>" /></td>
        </tr>
 
        <tr>
            <td>Producer</td>
            <td><input type='text' name='producer' class='form-control' required value="<?php echo isset($_POST['producer']) ? htmlspecialchars($_POST['producer'], ENT_QUOTES) : "";  ?>" /></td>
        </tr>
 
        <tr>
            <td>Created in</td>
            <td><input type='date' name='date' class='form-control' required value="<?php echo isset($_POST['date']) ? htmlspecialchars($_POST['date'], ENT_QUOTES) : "";  ?>" /></td>
        </tr>
 
        <tr>
            <td>Category</td>
            <td><input type='text' name='category' class='form-control' required value="<?php echo isset($_POST['category']) ? htmlspecialchars($_POST['category'], ENT_QUOTES) : "";  ?>" /></td>
 
        <tr>

            <td></td>
            <td>
                <button type="submit" class="btn btn-primary">
                    <span class="glyphicon glyphicon-plus"></span> Add
                </button>
            </td>
        </tr> 
 
    </table>
</form>
<?php
 
echo "</div>";
 

?>