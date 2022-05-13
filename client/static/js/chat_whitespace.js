document.addEventListener('DOMContentLoaded', function () {
    divs = document.querySelectorAll('.users');
    divs.forEach(function (div) {
        html = div.innerHTML;
        html = html.replace(/ /g, '');
        html = html.replace(/\r?\n|\r/g, '');
        html = html.replace(new RegExp(',', 'g'), ', ');
        console.log(html);
        div.innerHTML = html;
    });
});