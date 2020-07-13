document.addEventListener("DOMContentLoaded", function() {
    let combobox = document.getElementById("combobox");
    let input = document.getElementById("input-text");
    input.value = combobox.value;

    combobox.addEventListener("change", function() {
        let choice = combobox.value;
        input.value = choice;
        
    });

    input.addEventListener("focusout", function() {
        let options = combobox.options;
        if (input.value === "") {
            combobox.remove(combobox.selectedIndex);
        }
        else {
            options[combobox.selectedIndex].value = input.value;
            options[combobox.selectedIndex].innerHTML = input.value;
        }
    });

});
