$(document).ready(function() {

    $('.approveButton').click(function() {
        var catid;
        catid = $(this).attr("data-catid");
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationApproved/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.approveButton[data-catid=' + catid + '][user=' + userid + ']').html(data);
            //$('#approve').hide();
        });
    });

    $('.declineButton').click(function() {
        var catid;
        catid = $(this).attr("data-catid");
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationDeclined/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.declineButton[data-catid=' + catid + '][user=' + userid + ']').html(data);
            //$('#approve').hide();
        });
    });
/*
    $('.editButton').click(function() {
        var catid;
        var sessionid;
        var staus = 1;
        sessionid = $(this).attr("data-sessionid");
        $.get('/bookingsystem/manager/sessionInfoEdit/'+ sessionid, {
            //sessionID: sessionid,
            //type: 1
        }, function(data) {
            $('.editButton[data-sessionid=' + sessionid + ']').html("Submit");
            //$('#approve').hide();
        });
    });
*/
    $('.removeButton').click(function() {
        var catid;
        console.log('AAAAAA');
        catid = $(this).attr("data-catid");
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationDeleted/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.removeButton[data-catid=' + catid + '][user=' + userid + ']').html(data);
            //$('#approve').hide();
        });
    });

    $('.approveAllButton').click(function() {
        var catid;
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationAllApproved/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.approveAllButton[user=' + userid + ']').html(data);
            //$('#approve').hide();
        });
    });

    $('.declineAllButton').click(function() {
        var catid;
        userid = $(this).attr("user");
        $.get('/bookingsystem/manager/applicationAllDeclined/', {
            session_sessionid: catid,
            userid: userid
        }, function(data) {

            $('.declineAllButton[user=' + userid + ']').html(data);
            //$('#approve').hide();
        });
    });

     $("input[name=kidPaid26]").click(function() {
        $("#divEle").toggle();
    });

});