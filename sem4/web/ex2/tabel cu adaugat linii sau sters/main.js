function generate_table() {
    var content = '<table border="1">'
    content += '<thead><tr><th>Left</th>'
    for (i = 1; i <= 5; ++i) {
        content += '<th>Column ' + i + '</th>';
    }
    content += '<th>Right</th></tr></thead><tbody>'
    for (i = 1; i <= 5; ++i) {
        content += '<tr><td><button class="delete">delete</button ></td>'
        for (j = 1; j <= 5; ++j) {
            content += '<td>' + i +'</td>';
        }
        content += '<td><button class="insert">insert</button></td></tr>'
    }
    content += "</tbody></table>"
    $('#table-zone').append(content);
}

$(document).ready(function() {
    generate_table();

    $("#table-zone").on('click', '.delete', function() {
        let row = $(this).closest('tr');
        row.remove();
        //$("#table-zone tr:first").after("<tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td>");
    });

    $("#table-zone").on('click', '.insert', function() {
        let row = $(this).closest('tr');
        $("<tr>" + 
            "<td><button class=\"delete\">delete</button></td>" +
            "<td contenteditable='true'> </td>" + 
            "<td contenteditable='true'> </td>" + 
            "<td contenteditable='true'> </td>" + 
            "<td contenteditable='true'> </td>" + 
            "<td contenteditable='true'> </td>" + 
            "<td><button class=\"insert\">insert</button></td>" +
          "</tr>").insertAfter(row);
    });
    

    $('#table-zone').on('click', 'td', function() {
        var tdID = $(this).closest('td').index();
        if ( tdID == 0 || tdID == 6) {
            return;
        }
        let row = $(this).closest('tr');
        let full = true;
        row.find('td').each(function(i, td) {
            if (td.textContent ===  " ") {
                full = false;
            }
        });

        if (full === true) {
            $.each($(this).closest('tr').find('[contenteditable]'), function() {
                $(this).attr("contenteditable", "false");
              });
        }
    });

});