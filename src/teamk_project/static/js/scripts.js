
$(document).ready(function(){
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
});

function printContent(el){
	var restorepage = document.body.innerHTML;
	var printcontent = document.getElementById(el).innerHTML;
	document.body.innerHTML = printcontent;
	window.print();
	document.body.innerHTML = restorepage;
}

