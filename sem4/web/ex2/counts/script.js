$(function() {
    tables = $('.mytable');
    let new_table = "<table border='1'>";
    for(let i=0; i < tables.length; ++i){
        
        new_table += tables[i].innerHTML;
    }
    new_table += "</table>";
    $('#result').append(new_table);
});