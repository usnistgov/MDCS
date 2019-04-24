// Dropdowns.
var navbar;
var windowElement = $(window);
$( document ).ready(function(){
    navbar = $('#nav');
});

$('#nav > ul').dropotron({
    expandMode: "click",
    offsetY: -15,
    hoverDelay: 0,
    hideDelay: 500
});

windowElement.scroll(debounce(function (event) {
    if(windowElement.scrollTop() > 0){
        navbar.css(
            {
                position: 'fixed',
                top: 0
            });
    } else {
                navbar.css(
            {
                position: 'relative'
            });
    }
}, 100));