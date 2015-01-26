$(document).ready(function() {

	$('#approve').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/manager/applicationApproved/', {session_sessionid: catid}, function(data){
        	$('#approve').html(data);  
           });
	});

});