
$(document).ready(function(){
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
        

	   if ($(window).width() < 390) {
		   $( ".navbar-brand" ).replaceWith( "<a class='navbar-brand' href='/'>WTC</a>" );
		}
		else {
			   $( ".navbar-brand" ).replaceWith( "<a class='navbar-brand' href='/'>Western  Tennis Club</a>" );
			}


});


$(window).resize(function() {
  if ($(window).width() < 390) {
	   $( ".navbar-brand" ).replaceWith( "<a class='navbar-brand' href='/'>WTC</a>" );
	}
	else {
	   $( ".navbar-brand" ).replaceWith( "<a class='navbar-brand' href='/'>Western  Tennis Club</a>" );
	}
});

function printContent(el){
	var restorepage = document.body.innerHTML;
	var printcontent = document.getElementById(el).innerHTML;
	document.body.innerHTML = printcontent;
	window.print();
	document.body.innerHTML = restorepage;
}

