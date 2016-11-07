// Create a clone of the menu, right next to original.
var $menuOriginal = $('#nav');
$menuOriginal.addClass('original');

var $menuCloned = $menuOriginal.clone();
$menuCloned.addClass('cloned');
$menuCloned.removeClass('original');

$menuCloned.css({
    'position': 'fixed',
    'top': '0',
    'margin-top': '0',
    'z-index': '500',
});

$menuCloned.hide();
$menuCloned.insertAfter($menuOriginal);

// Configure the scroll check
scrollIntervalID = setInterval(stickIt, 10);

var hiddenDropdown = true;

function stickIt() {
    var orgElementPos = $('.original').offset();
    orgElementTop = orgElementPos.top;

    if ($(window).scrollTop() >= (orgElementTop)) {
        // scrolled past the original position; now only show the cloned, sticky element.

        // Cloned element should always have same left position and width as original element.
        orgElement = $('.original');
        coordsOrgElement = orgElement.offset();
        leftOrgElement = coordsOrgElement.left;
        widthOrgElement = orgElement.css('width');
        $('.cloned').css('left',leftOrgElement+'px').css('top',0).css('width',widthOrgElement).show();
        $('.original').css('visibility','hidden');

        if( hiddenDropdown ) {


            hiddenDropdown = false;
        }

    } else {
        // not scrolled past the menu; only show the original menu.
        $('.cloned').hide();
        //$('.cloned > ul').dropotron();
        $('.original').css('visibility','visible');
    }
}

// Dropdowns.
$('.original > ul').dropotron({
    expandMode: "click",
    offsetY: -15,
    hoverDelay: 0,
    hideDelay: 500
});

$('.cloned > ul').dropotron({
    expandMode: "click",
    offsetY: -15,
    hoverDelay: 0,
    hideDelay: 500
});