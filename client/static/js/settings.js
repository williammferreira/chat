if (window.location.protocol === "https") {
    const searchSocket = new WebSocket('wss://' + window.location.host + '/ws/search');
} else {
    const searchSocket = new WebSocket('ws://' + window.location.host + '/ws/settings');
}

var theme = "";

function themeSlider(theme) {
    if (theme == "dark") {
        // themeLabelDark
        executeAsync(function() {
            var animationId;
            var label = $("#themeLabelDark");
            var rgb = 0;
            function fade() {
                if (window.getComputedStyle(label, null).color == "rgb(255, 255, 255)") {
                    cancelAnimFrame(animationId);
                    return;
                }
                rgb += 5;
                label.style.color = "rgb(" + rgb + ", " + rgb + ", " + rgb + ")";

                animationId = requestAnimFrame(fade);
            }
            fade();
        });

        // themeLabelLight
        executeAsync(function() {
            var animationId;
            var label = $("#themeLabelLight");
            var rgb = 255;
            function fade() {
                if (window.getComputedStyle(label, null).color == "rgb(0, 0, 0)") {
                    cancelAnimFrame(animationId);
                    return;
                }
                rgb -= 5;
                label.style.color = "rgb(" + rgb + ", " + rgb + ", " + rgb + ")";

                animationId = requestAnimFrame(fade);
            }
            fade();
        });
        
        // themeSlider
        executeAsync(function() {
            var speed = 20;
            node = $("#themeSlider");
            var pos = parseInt(String(window.getComputedStyle(node, null).marginRight).slice(0, -2));
            var endPos = $("#themeLabel").offsetWidth;
            var animationId;
            function animate() {
                if (pos >= (endPos / 2)) {
                    cancelAnimFrame(animationId);
                    return;
                } else if ((pos + speed) > (endPos / 2)) {
                    pos += (endPos / 2) - pos;
                } else {
                    pos += speed;
                }
                node.style.left = pos + "px";
                animationId = requestAnimFrame(animate);
            }
        
            animate();
        });
    } else {

        // themeLabelDark
        executeAsync(function() {
            var animationId;
            var label = $("#themeLabelDark");
            var rgb = 255;
            function fade() {
                if (window.getComputedStyle(label, null).color == "rgb(0, 0, 0)") {
                    cancelAnimFrame(animationId);
                    return;
                }
                rgb -= 5;
                label.style.color = "rgb(" + rgb + ", " + rgb + ", " + rgb + ")";

                animationId = requestAnimFrame(fade);
            }
            fade();
        });

        // themeLabelLight
        executeAsync(function() {
            var animationId;
            var label = $("#themeLabelLight");
            var rgb = 0;
            function fade() {
                if (window.getComputedStyle(label, null).color == "rgb(255, 255, 255)") {
                    cancelAnimFrame(animationId);
                    return;
                }
                rgb += 5;
                label.style.color = "rgb(" + rgb + ", " + rgb + ", " + rgb + ")";

                animationId = requestAnimFrame(fade);
            }
            fade();
        });
        
        // themeSlider
        executeAsync(function() {
            var speed = 20;
            node = $("#themeSlider");
            var pos = 0;
            var endPos = $("#themeLabel").offsetWidth;
            var animationId;
            function animate() {
                if (pos >= (endPos / 2)) {
                    cancelAnimFrame(animationId);
                    return;
                } else if ((pos + speed) > (endPos / 2)) {
                    pos += (endPos / 2) - pos;
                } else {
                    pos += speed;
                }
                node.style.left = ((endPos / 2) - pos) + "px";
                animationId = requestAnimFrame(animate);
            }

            animate();
        });
    }
    
}

function setTheme(setting, value) {
    if (setting == "theme") {
        if (theme == "") {
            if (value == "dark") {
                value = "light";
            } else {
                value = "dark";
            }
            setSetting("theme", value);
            theme = value;
            themeSlider(value);
        } else {
            if (theme == "dark") {
                theme = "light";
                setSetting("theme", "light");
                themeSlider("light");
            } else {
                theme = "dark";
                setSetting("theme", "dark");
                themeSlider("dark");
            }
            
        }
    }
}

function setSetting(name, value) {
    settingSocket.send(JSON.stringify({
        "setting": name,
        "value": value,
    }));
}