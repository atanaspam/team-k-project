$(document).ready(function() {
	
    $('.approveButton').click(function() {
    	console.log("NASKOOOOO");
        var catid;
        catid = $(this).attr("data-catid");
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationApproved/', {
            session_sessionid: catid,
            userid:userid
        }, function(data) {

            $('.approveButton[data-catid='+catid+']').html(data);
            //$('#approve').hide();
        });
    });

});