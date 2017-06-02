function loadActionTiles() {
    $.ajax({
        url: tilesGetUrl,
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
        url: templatesGetUrl,
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