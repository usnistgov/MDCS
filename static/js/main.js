/*
	Arcana by HTML5 UP
	html5up.net | @n33co
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/
(function($) {
	$(function() {
		let	$body = $('body');

		// Disable animations/transitions until the page has loaded.
        setTimeout(function(){
            $(document).ready( function() {
                $body.removeClass('is-loading');
            });
        });

        $body.addClass('is-loading');
        $('form').placeholder();  // Fix: Placeholder polyfill.

        // Title Bar.
        $(
            '<div id="titleBar">' +
                '<a href="#navPanel" class="toggle"><i class="fas fa-bars ml-2"></i></a>' +
                '<span class="title">' + $('#cdcs-menu-title a').html() + '</span>' +
            '</div>'
        ).prependTo('#page-wrapper');

        // Navigation Panel.
        $(
            '<div id="navPanel">' +
                '<nav>' +
                    $('#nav').navList() +
                '</nav>' +
            '</div>'
        )
            .appendTo($body)
            .panel({
                delay: 500,
                hideOnClick: true,
                hideOnSwipe: true,
                resetScroll: true,
                resetForms: true,
                side: 'left',
                target: $body,
                visibleClass: 'navPanel-visible'
            });
	});
})(jQuery);