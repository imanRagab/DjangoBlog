$(function(){

/////////////////////////////////////////
    $("#likeBtn").click(function(){
        if($(this).html() == "Like"){

          $("#likesCount").html(parseInt($("#likesCount").html()) + 1)

         $(this).html("Unlike");
         thiss=this
        $("#dislikeBtn").attr("disabled","disabled")
         $.ajax({
            url: '/ourblog/like/'+$(this).attr("postId")+'/',
            type: 'get',
            data: {
                post_id: $(thiss).attr("postId") },
            success: function(reponse){
                    console.log(reponse)
                    // alert("liked")

                    },
            error: function (error) {
                // alert(error);
                }
                });

         } else {

           $("#likesCount").html(parseInt($("#likesCount").html() - 1))

           $(this).html("Like")
           $("#dislikeBtn").removeAttr("disabled")
            thiss=this
           $.ajax({
            url: '/ourblog/unlike/'+$(this).attr("postId")+'/',
            type: 'get',
            data: {
            post_id: $(thiss).attr("postId") },
            success: function(reponse){
                    console.log(reponse)
                    // alert("unliked")

                    },
            error: function (error) {
                // alert(error);
                }
                });
         }
    });
    ///////////////////////////////////////
    $("#dislikeBtn").click(function(){

      if($(this).html()== "Dislike" ){

        $("#dislikesCount").html(parseInt($("#dislikesCount").html()) + 1)

       $(this).html("Undislike")
       $("#likeBtn").attr("disabled","disabled")
        thiss=this
        $.ajax({

        url: '/ourblog/dislike/'+$(this).attr("postId")+'/',
        type: 'get',
        data: {
            post_id: $(thiss).attr("postId")
        },
        success: function(reponse){
           console.log(reponse)
                // alert("disliked!")
        },
        error: function (error) {

                // alert(error);
                }
        });

 }

else {

            $("#dislikesCount").html(parseInt($("#dislikesCount").html()) - 1)

             $(this).html("Dislike")
             $("#likeBtn").removeAttr("disabled")
             thiss=this
             $.ajax({

                url: '/ourblog/undislike/'+$(this).attr("postId")+'/',
                type: 'get',
                data: {
                        post_id: $(this).attr("postId")
                    },
                success: function(reponse){
                             console.log(reponse)
                            // alert("un-disliked!")
                    },
                error: function (error) {
                            // alert(error);
                            }
                    });
            }
    });

///////////////////////////////////////////////

    $(".subs").click(function(){
    cat_id = $(this).attr("data1");
    console.log("cat"+cat_id);
    user_id = $(this).attr("data2");
    console.log("user"+user_id);
	if( $(this).html() == "Subscribe" )
	{
		$(this).html("UnSubscribe");
		$.ajax({
        url: '/ourblog/sup/'+ cat_id + '/' +user_id + '/' ,
        success: function(){
            console.log("ana geeeeet");
        }
    });
	}
	else
	{
		$(this).html("Subscribe");
		$.ajax({
        url: '/ourblog/unsup/'+ cat_id + '/' +user_id + '/' ,
        success: function(){
            console.log("ana mageeeeetsh");
        }
    });
	}
	$(this).toggleClass('btn-secondary');
	$(this).toggleClass('btn-danger');
    });

/////////////////////////////////////////////

$("#search").on("keyup",function(){
                searchlist = $("#searchlist");
            $.ajax({
                url: '/ourblog/search/'+$(this).val(),
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


////////////////////////////////////////////

function searchItem(PostData){
    console.log(PostData);
    return $('<li class="searchitem"><a href="/ourblog/post/'+PostData.pk+'">'+PostData.fields.post_title+'</a></li>');
}


});
