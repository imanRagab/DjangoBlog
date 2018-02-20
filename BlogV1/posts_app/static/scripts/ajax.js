$(function(){



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

    var current_comment_id

    });

    /////////////////////////////////////////

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
        success: function(response){
             alert("disliked!")
                console.log(response)
           response=JSON.parse(response)
           count=response.count
           if (count == 10){
                 $("#exampleModal").modal('show');
           }

        },
        error: function (error) {

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
                            }
                    });
            }


    });


    $("#loginForm").submit(function(){

        $.ajax({

            type: $("#loginForm").attr("method"),
            url: $("#loginForm").attr("action"),
            data: $("#loginForm").serialize(),
            success: function(resp){

            }
        });
    });

    $("#search").on("keyup",function(){
                    searchlist = $("#searchlist");
                $.ajax({
                    url: 'http://127.0.0.1:8000/ourblog/search/'+$(this).val(),
                    type: 'get',
                    success: function(response){
                        data = JSON.parse(response);
                        console.log(data);

                    searchlist.html("");
                        $(data).each(function(){
                            searchlist.append(searchItem(this));
                        });
                    },
                    error:function(){
                    searchlist.html("");
                    },
            });
    });


    function searchItem(PostData){
        console.log(PostData);
        return $('<li class="searchitem"><a href="http://127.0.0.1:8000/ourblog/post/'+PostData.pk+'">'+PostData.fields.post_title+'</a></li>');
    }


});