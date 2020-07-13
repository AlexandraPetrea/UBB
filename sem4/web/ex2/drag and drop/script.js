var allNodes = document.querySelectorAll(".container *");
var dragged = undefined;
allNodes.forEach(function (element) {
    element.draggable = true;
    element.addEventListener("dragstart", function (event) {
        console.log(event.target);
        dragged = event.target;
    }, false);
    element.addEventListener("dragenter", function (event) {
        event.preventDefault();
    });
    element.addEventListener("dragover", function (event) {
        event.preventDefault();
    });
    element.addEventListener("drop", function (event) {
        if (dragged !== event.target) {
            var boundingClientRect = event.target.getBoundingClientRect();
            var factor = (event.pageY - boundingClientRect.top) / boundingClientRect.height;

            var target = "afterend";

            if (factor < .25) {
                target = "beforebegin";
            } else if (factor < .5) {
                target = "afterbegin";
            } else if (factor < .75) {
                target = "beforeend";
            }

            event.target.insertAdjacentElement(target, dragged);
            dragged = undefined;
        }
    }, false);
});