<%--
  Created by IntelliJ IDEA.
  User: todor
  Date: 7/12/2018
  Time: 10:47 AM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

<div class="container">
<form style="margin-left: 15px; margin-top: 20px;" method="post" action="/AddServlet">
    <table>
        <td style="border: black">
            <label for="idobject">IdObject: </label>
            <input class="form-control" type="text" name="idobject" id="idobject"/>
            <br/>
            <label for="iduser">IdUser: </label>
            <input class="form-control" type="text" name="iduser" id="iduser"/>
            <br/>
            <label for="text">Text: </label>
            <textarea class="form-control" type="text" name="text" id="text" cols="40" rows="5"></textarea>

            <br/>
        </td>


    </table>
    <input class="btn btn-danger" type="submit" value="Add"/>
</form>
</div>
</html>
