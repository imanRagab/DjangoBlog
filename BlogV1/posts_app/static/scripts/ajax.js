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


    $("#sendReply").click(function(){


        $.ajax({

        url: '',
        type: 'post',
        data: {},
        success: function(){





        }



        });

    });


    ///////////////////////////////////////

    $("#likeBtn").click(function(){


        $.ajax({

        url: '/likepost',
        type: 'post',
        data: {

            type: 1,
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

            type: 0,
            post_id: $(this).attr("postId")

        },
        success: function(){





        }



        });

    });

});


