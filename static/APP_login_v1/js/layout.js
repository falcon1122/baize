/*
layout-relayted js file
by tayir 
email:arnoldincredible@126.com
*/
var windowHeight = $(window).height();
function footerFixBottom() {
	if($(document.body).height() < windowHeight){
	  $("footer").addClass('navbar-fixed-bottom');
	}else{
	  $("footer").removeClass('navbar-fixed-bottom');
	}
}
footerFixBottom();
$(window).resize(footerFixBottom);