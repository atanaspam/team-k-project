$(document).ready(function() {

    $('.approveButton').click(function() {
        //console.log("NASKOOOOO");
        var catid;
        catid = $(this).attr("data-catid");
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationApproved/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.approveButton[data-catid=' + catid + ']').html(data);
            //$('#approve').hide();
        });
    });

    // Not working for some reason :(
    $('.infoButton').click(function() {
        console.log("This is not a viable solution to get the session info.");
        var catid;
        catid = $(this).attr("data-sessionid");
        $.get('/bookingsystem/manager/sessionInfo/', {
            session_sessionid: catid,
        }, function(data) {

            //$('.infoButton[data-catid='+catid+']').html(data);
            //$('#approve').hide();
        });
    });

});