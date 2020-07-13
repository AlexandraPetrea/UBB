<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<div class="container">
    <form style="margin-left: 15px; margin-top: 20px;" method="post" action="/VoteServlet">
        <div class="row">
            <div class="col-md-5">
                <label for="title">Title: </label>
                <input type="text" name="title" id="title"/>
                <input class="btn btn-danger" type="submit" value="Vote"/>
            </div>

        </div>
    </form>
</div>
</html>
