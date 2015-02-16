$(document).ready(function(){
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');

  });
});

function populateChildCheckboxes()
{
	var div = document.createElement('div');
	div.class = checkbox;
	div.id = "id";

	var checkbox = document.createElement('input');
	checkbox.type = "checkbox";
	checkbox.class = "checkbox";
	checkbox.name = "name";
	checkbox.value = "value";
	checkbox.id = "id";

	var label = document.createElement('label')
	label.htmlFor = "id";
	label.appendChild(document.createTextNode('text for label after checkbox'));

	div.appendChild(checkbox);
	div.appendChild(label);

	childrenCheckboxes.appendChild(div);
}

