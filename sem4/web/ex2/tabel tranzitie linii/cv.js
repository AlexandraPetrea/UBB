var divs = new Array("a","b","c","d","e","f");

var content = document.getElementById("content");
// Original
for(var i = 0; i < divs.length; i++){
    var div = document.createElement("div");
    div.appendChild(document.createTextNode(divs[i]));
    div.setAttribute("id", divs[i]);
    content.appendChild(div);
}

// Reverse
divs.reverse();
for(var i = 0; i < divs.length; i++){
    var div = document.createElement("div");
    div.appendChild(document.createTextNode(divs[i]));
    div.setAttribute("id", divs[i]);
    content.appendChild(div);
}