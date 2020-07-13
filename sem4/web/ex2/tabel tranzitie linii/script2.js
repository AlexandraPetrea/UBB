let element = document.body;
for (var i = 1; i < element.childNodes.length; i++) {
  element.insertBefore(element.childNodes[i], element.firstChild);
}