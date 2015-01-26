$(document).ready(function() {

	$('#approve').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
     $.get('/bookingsystem/manager/applicationApproved/', {session_sessionid: catid}, function(data){
        	$('#approve').html(data); 
        	$('#approve').hide(); 
           });
	});

});