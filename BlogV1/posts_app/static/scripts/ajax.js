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
    var current_comment_id
    });
    /////////////////////////////////////////
    $("#likeBtn").click(function(){
        $.ajax({
            url: '/ourblog/likepost',
            type: 'get',
            data: {
                post_id: $(this).attr("postId")
            },
            success: function(resp){
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

 });