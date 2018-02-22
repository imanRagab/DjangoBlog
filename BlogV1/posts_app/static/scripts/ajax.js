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
    var current_comment_id;
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
    ///////////////////////////////////////////////
    $(".subs").click(function(){
    cat_id = $(this).attr("data1");
    console.log(cat_id);
    user_id = $(this).attr("data2");
    console.log(user_id);
	if( $(this).html() == "Subscribe" )
	{
		$(this).html("UnSubscribe");
		$.ajax({
        url: 'http://127.0.0.1:8000/ourblog/sup/'+ cat_id + '/' +user_id + '/' ,
        success: function(){
            console.log("ana geeeeet");
        }
    });
	}
	else
	{
		$(this).html("Subscribe");
		$.ajax({
        url: 'http://127.0.0.1:8000/ourblog/unsup/'+ cat_id + '/' +user_id + '/' ,
        success: function(){
            console.log("ana mageeeeetsh");
        }
    });
	}
	$(this).toggleClass('btn-primary');
	$(this).toggleClass('btn-danger');
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
