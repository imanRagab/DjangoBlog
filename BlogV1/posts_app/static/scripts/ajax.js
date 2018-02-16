$(function(){

    ////////////////////////////////////////////

    $("#sendComment").click(function(){


        $.ajax({

        url: '',
        type: 'post',
        data: {},
        success: function(){





        }



        });

    });

    /////////////////////////////////////////


    $("#sendReply").on('click', function(e){

        e.preventDefault()
        alert("hi")

//        $.ajax({
//
//            url: '/ourblog/commentreply',
//            type: 'get',
//            data: {
//
//                comment_id: $(this).attr("commentId")
//                reply_text: $("#reply_text").val()
//
//                },
//
//            success: function(resp){
//
//                alert(resp);
//            }
//
//        });
//    });


    ///////////////////////////////////////

    $("#likeBtn").click(function(){


        $.ajax({

        url: '/likepost',
        type: 'post',
        data: {

            post_id: $(this).attr("postId")

        },
        success: function(){





        }



        });

    });

    ///////////////////////////////////////

    $("#dislikeBtn").click(function(){


        $.ajax({

        url: '/likepost',
        type: 'post',
        data: {

            post_id: $(this).attr("postId")

        },
        success: function(){





        }



        });

    });

    /////////////////////////////////////

    $("#commentForm").submit(function(){


        $.ajax({

            type: $("#commentForm").attr("method"),
            url: $("#commentForm").attr("action"),
            data: $("#commentForm").serialize(),
            success: function(resp){
                alert(resp);
            }



        });



    });



    /////////////////////////////////////

    $("#subs").click(function(){

        if($(this).html() == "Subscribe")
            $(this).html("UnSubscribe");

        else
            $(this).html("Subscribe");

        $(this).toggleClass('btn-primary');
        $(this).toggleClass('btn-danger');
    });

});


