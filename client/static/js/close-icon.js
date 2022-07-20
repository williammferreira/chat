var img = document.getElementById("close_img");
var img_wrapper = document.getElementById("close_image_wrapper");
var img_default = img.getAttribute("data-src-default");
var img_black = img.getAttribute("data-src-black");

img_wrapper.addEventListener("mouseover", function (e) {
    img.src = img_black;
});

img_wrapper.addEventListener("mouseout", function (e) {
    img.src = img_default;
});