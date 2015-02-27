
$(document).ready(function(){
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });

if ($(window).width() < 960) {
   $( ".navbar-brand" ).replaceWith( "<a class='navbar-brand' href='/'>WTC</a>" );
}

});

function printContent(el){
	var restorepage = document.body.innerHTML;
	var printcontent = document.getElementById(el).innerHTML;
	document.body.innerHTML = printcontent;
	window.print();
	document.body.innerHTML = restorepage;
}

