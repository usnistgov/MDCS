function loadActionTiles() {
    $.ajax({
        url: "/home/tiles",
        method: "GET",
        success: function(data) {
            $("#tiles").html(data);
        },
        error: function(data) {

        },
    });
}


function loadTemplateList() {
    $.ajax({
        url: "/home/templates",
        method: "GET",
        success: function(data) {
            $("#templates").html(data);
        },
        error: function(data) {

        },
    });
}

loadActionTiles();
loadTemplateList();