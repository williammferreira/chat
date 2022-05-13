var time = document.getElementById('time');
var controls = document.getElementById('controls');
var mouseOver = false;

controls.addEventListener('mouseover', function (evt) {
    setInterval(() => {
        if (mouseOver) {
            now = new Date();
            months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']
            month = months[now.getMonth()]

            ispm = now.getHours() == 12 ? true : now.getHours() > 12;

            time.innerHTML = month + ' ' + now.getDate() + ', ' + now.getFullYear() + ' ' + (ispm ? now.getHours() - 12 : now.getHours()) + ':' + (now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()) + ' ' + (ispm ? 'PM' : 'AM');
        } else {
            time.innerHTML = '';
        }
    }, 100);
});

controls.addEventListener('mouseover', function (evt) {
    mouseOver = true;
}, true);

controls.addEventListener('mouseout', function (evt) {
    mouseOver = false;
});