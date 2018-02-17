$(function(){

    ////////////////////////////////////////////

//    $("#sendComment").click(function(){
//
//
//        $.ajax({
//
//        url: '',
//        type: 'post',
//        data: {},
//        success: function(){
//
//
//
//
//
//        }
//
//
//
//        });
//
//    });

    /////////////////////////////////////////


//    $("#sendReply").on('click', function(e){
//
//        e.preventDefault()
//        alert("hi")

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



        if($(this).html() == "Like"){

         $(this).html("Unlike");
         thiss=this
        $("#dislikeBtn").attr("disabled",true)
         $.ajax({
            url: 'http://127.0.0.1:8000/ourblog/like/'+$(this).attr("postId")+'/',
            type: 'get',
            data: {
                post_id: $(thiss).attr("postId") },
            success: function(reponse){
                    console.log(reponse)
                    alert("liked")

                    },
            error: function (error) {
                alert(error);
                }
                });

         } else {

           $(this).html("Like")
           $("#dislikeBtn").attr("disabled",false)
            thiss=this
           $.ajax({
            url: 'http://127.0.0.1:8000/ourblog/unlike/'+$(this).attr("postId")+'/',
            type: 'get',
            data: {
            post_id: $(thiss).attr("postId") },
            success: function(reponse){
                    console.log(reponse)
                    alert("unliked")

                    },
            error: function (error) {
                alert(error);
                }
                });
         }

    });

    ///////////////////////////////////////

    $("#dislikeBtn").click(function(){


      if($(this).html()== "Dislike" ){

       $(this).html("Undislike")
       $("#likeBtn").attr('disabled',true)
        thiss=this
        $.ajax({

        url: 'http://127.0.0.1:8000/ourblog/dislike/'+$(this).attr("postId")+'/',
        type: 'get',
        data: {
            post_id: $(thiss).attr("postId")
        },
        success: function(reponse){
           console.log(reponse)
                alert("disliked!")
        },
        error: function (error) {

                alert(error);
                }
        });

 }

else {

             $(this).html("Dislike")
             $("#likeBtn").attr('disabled',false)
             thiss=this
             $.ajax({

                url: 'http://127.0.0.1:8000/ourblog/undislike/'+$(this).attr("postId")+'/',
                type: 'get',
                data: {
                        post_id: $(this).attr("postId")
                    },
                success: function(reponse){
                             console.log(reponse)
                            alert("un-disliked!")
                    },
                error: function (error) {
                            alert(error);
                            }
                    });
            }


    });

//    /////////////////////////////////////
//
//    $("#subs").click(function(){
//
//        if($(this).html() == "Subscribe")
//            $(this).html("UnSubscribe");
//
//        else
//            $(this).html("Subscribe");
//
//        $(this).toggleClass('btn-primary');
//        $(this).toggleClass('btn-danger');
//    });
//


});
