var img = document.getElementById("close_img");
var img_wrapper = document.getElementById("close_image_wrapper");
var img_default = img.getAttribute("data-src-default");
var img_black = img.getAttribute("data-src-black");

var select = document.getElementsByClassName("selected-user")[0];
var select_options = document.getElementsByTagName("option");
var options = document.querySelectorAll(".select-option");
var options_wrapper = document.getElementById("select-options");
var select_wrapper = document.getElementsByClassName("select-wrapper")[0];
var caret = document.getElementsByClassName("caret")[0];
var selected_user = document.getElementsByClassName("user")[0];
var select_clicked = false;


img_wrapper.addEventListener("mouseover", function (e) {
    img.src = img_black;
});

img_wrapper.addEventListener("mouseout", function (e) {
    img.src = img_default;
});

function handleTransferClicked() {
    var dialog = document.getElementById("transfer-dialog")
    dialog.showModal();
    dialog.classList.add("transfer-dialog-open");
}

function getElementWithAttribute(node_list, attr, value) {
    for (let i = 0; i < node_list.length; i++) {
        const node = node_list[i];
        if (node.getAttribute(attr) == value) {
            return node;
        }
    }
}

select.addEventListener("click", function (e) {
    if (select_clicked) {
        caret.style.transition = "transform 500ms";
        caret.style.transform = "rotateZ(-90deg)";

        options_wrapper.style.display = "none";

        select_clicked = false;
    } else {
        caret.style.transition = "transform 500ms";
        caret.style.transform = "rotateZ(-180deg)";

        options_wrapper.style.display = "block";

        select_clicked = true;
    }
});

document.addEventListener("click", function (e) {
    if (select_clicked && e.target != select) {
        caret.style.transition = "transform 500ms";
        caret.style.transform = "rotateZ(-90deg)";

        options_wrapper.style.display = "none";

        select_clicked = false;
    }
});

function setOptionsClicked() {
    options.forEach(function (option) {
        setOptionClickedListener(option);
    });
}

function setOptionClicked(evt, option) {
    var unselected_user = selected_user.innerHTML;

    selected_user.innerHTML = option.innerHTML;
    option.remove();

    console.log(select_options[0].selected);
    console.log(select_options[1].selected);
    Array.from(select_options).filter(option => option.selected)[0].selected = false;

    Array.from(select_options).filter(option => {
        if (option.innerText.trim() == selected_user.innerText.trim()) {
            option.selected = true;
        }
    });

    var unselected_option = document.createElement("option");
    unselected_option.classList.add("select-option");
    unselected_option.innerHTML = unselected_user;

    setOptionClickedListener(unselected_option);

    options_wrapper.appendChild(unselected_option);

}

function setOptionClickedListener(option) {
    option.addEventListener("click", (e) => {
        setOptionClicked(e, option);
    });
}

setOptionsClicked();