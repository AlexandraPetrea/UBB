<%--
  Created by IntelliJ IDEA.
  User: todor
  Date: 7/12/2018
  Time: 12:26 PM
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Pag</title>
</head>
<body>
    <form style="margin-left: 15px; margin-top: 20px;">

        <div id='entries-section'></div>
        <br>

        <h4>Paginated:</h4>

        <div id='entries-section2'></div>
        <button onclick="getall()">Prev</button>
        <button onclick="prev()">Prev</button>
        <button onclick="next()">Next</button>
    </form>
</body>

<script>

    function getAll(page, callbackFunction){
        $.getJSON(
            "BiblioController",
            {
                action : "getAll",
                page: page
            },
            callbackFunction
        )
    }


    /// /AJAX
    var page = 1;

    function next(){
        page += 1;
        searchByTitleOrAuthorPaged(page)
    }

    function prev(){
        page -= 1;
        searchByTitleOrAuthorPaged(page);
    }

    function search(){
        searchByTitleOrAuthorPaged(page);
    }


    function searchByTitleOrAuthorPaged(page) {
        getAll(page, function(response) {
            console.log(response);
            displayEntries(response);
        })
    }


    function displayEntries(entries){
        $("#entries-section2").html("<div id='entries-section2'>");

        for (var entry in entries) {
            entry = entries[entry];
            console.log(entry);
            $("#entries-section2").append(
                "<p>"
                + "<span>"+ entry["ID"] +"</span>"
                + "<span>"+ entry["Author"]+"</span>"
                + "<span>"+ entry["Title"] +"</span>"
                + "<span>"+ entry["Text"] +"</span>"
                + "<span>"+ entry["Votes"] +"</span>"
                + "</p></br>")
        }

        $("#entries-section2").append("</div>");
    }
</script>

</html>
