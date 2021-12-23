document.onload = (
    function() {
        fitText($("#dashboardLink"), 20);

        if (window.innerHeight <= 1050) {
            fitText($("#settingsUsername"), 60);
        } else {
            $("#settingsUsername").style.fontSize = "40px";
        }

        window.onresize = function() {
            fitText($("#dashboardLink"), 20);


            if (window.innerHeight <= 1050) {
                fitText($("#settingsUsername"), 60);
            }
        }
    }
)()