$(function(){

    $("#subs").click(function(){

        if($(this).html() == "Subscribe")
            $(this).html("UnSubscribe");

        else
            $(this).html("Subscribe");

        $(this).toggleClass('btn-primary');
        $(this).toggleClass('btn-danger');
    });

});


