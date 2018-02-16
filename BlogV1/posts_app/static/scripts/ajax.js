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

});


