var last_index = 0;

function show(index) {
  if(last_index != 0) {
    document.getElementById("content_" + last_index).style.display = "none";
  }
  document.getElementById("content_" + index).style.display = "block";
  last_index = index;
}