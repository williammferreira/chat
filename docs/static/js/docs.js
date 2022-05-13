const docsWebsocket = new WebSocket('ws://127.0.0.1:8000/ws/docs/DocsConsumer');

docsWebsocket.onopen = function () {
    console.info('WebSocket connect');
};

docsWebsocket.onmessage = function (rawData) {
    var data = JSON.parse(rawData.data);

    var children = JSON.parse(data.children);

    console.log('message recieved: ' + JSON.stringify(children));

    console.log(JSON.stringify(children[0].fields.title));

    children.forEach(function (object, index) {
        console.log(JSON.stringify(object));
        let container = document.createElement('div');
        container.setAttribute('class', 'group');
        container.setAttribute('id', object.pk);

        let chevron = document.createElement('img');
        chevron.setAttribute('src', '/static/images/chevron-right-blue.png');
        chevron.setAttribute('alt', 'Chevron Right');
        chevron.setAttribute('height', '20px');
        chevron.setAttribute('class', 'chevron-right');

        let title = document.createElement('span');
        title.innerText = object.fields.title;

        container.appendChild(chevron, title);

        document.getElementById().appendChild(container);
    })

    document.querySelectorAll(".group").forEach(function (group) {
        group.addEventListener('click', function () {
            docsWebsocket.send(JSON.stringify({
                'id': group.id,
            }));
        });
    });
};