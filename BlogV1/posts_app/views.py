from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import Post, Category, Comment, Tag, Reply, Like, Dislike, Forbidden, CategorySubscribtion, PostsTags
from forms import ReplyForm, CommentForm

####################################################################

def post(request, post_id):

    comment_form = CommentForm()
    reply_form = ReplyForm()
    try:
        post = Post.objects.get(id=post_id)
        tags = PostsTags.objects.filter(post=post_id)
        post_tags = []
        categories = Category.objects.all()
        if post:
            comments = Comment.objects.filter(comment_post__id=post_id)
            likes = len(Like.objects.filter(like_post__id=post_id))
            dislikes = len(Dislike.objects.filter(dislike_post__id=post_id))
            like_state = is_liked(request, post_id)
            dislike_state = is_disliked(request, post_id)
            forbidden_words = Forbidden.objects.all()
            comments_replies = []

            if tags:
                for tag in tags:
                    post_tags.append(Tag.objects.get(id=tag.id))


            if comments:
                for comment in comments:  ## check comments for forbidden words
                    for forbidden_word in forbidden_words:
                        comment.comment_text = comment.comment_text.replace(forbidden_word.word,
                                                                            ("*" * len(forbidden_word.word)))
                    replies = Reply.objects.filter(reply_comment__id=comment.id)
                    comments_replies.append(replies)

                if replies:

                    for reply in replies:  ## check replies for forbidden words
                        for forbidden_word in forbidden_words:
                            reply.reply_text = reply.reply_text.replace(forbidden_word.word, ("*" * len(forbidden_word.word)))

            context = {'post': post, 'categories': categories,
                       'comments': comments, 'replies': comments_replies,
                       'comment_form': comment_form,
                       'reply_form': reply_form,
                       'likes': likes,
                       'dislikes': dislikes,
                       'tags': post_tags,
                       'like_state': like_state,
                       'dislike_state': dislike_state}

    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'post.html', context)

######################################################

def home(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by('-post_created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    page_posts = paginator.page(page)
    retCats = []
    for cat in categories:
        retCats.append({"state": is_supped(request, cat.id), "cat": cat})
    # posts_all = Post.objects.order_by('post_created_at')
    context = {'categories': retCats, 'page_posts': page_posts, 'Like': Like, 'Dislike': Dislike}

    return render(request, 'home.html', context)


#####################################################

def category(request, cat_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=cat_id)
    retCats = []
    for cat in categories:
        retCats.append({"state": is_supped(request, cat.id), "cat": cat})
        # retCats.append({"state":is_supped(request,cat.id),"cat":serializers.serialize('json',[cat])})
    # return JsonResponse(retCats, safe=False)
    sub_state = is_supped(request, cat_id)
    # return HttpResponse(category)
    cat_posts = Post.objects.filter(post_category__id=cat_id)
    paginator = Paginator(cat_posts, 10)  # Show 10 posts per page
    if request.GET.get('page'):
        page = request.GET.get('page')
    else:
        page = 1
    page_posts = paginator.page(page)

    # cat_post = map(lambda x : x, cat_posts)
    context = {'category': category, 'sub_state': sub_state, 'categories':retCats,'page_posts': page_posts}

    return render(request, 'category.html', context)


#####################################################

def comment_reply(request, post_id, comment_id):
    if request.method == 'GET':
        reply_text = request.GET['reply_text']

        # forbidden_words = Forbidden.objects.all()
        #
        # for forbidden_word in forbidden_words:
        #     reply_text = reply_text.replace(forbidden_word.word, ("*" * len(forbidden_word.word)))

        comment = Comment.objects.get(pk=comment_id)
        reply = Reply(reply_comment=comment, reply_text=reply_text, reply_user=request.user)
        reply.save()
        return HttpResponseRedirect('/ourblog/post/' + post_id)

    else:
        return HttpResponse("Request method is not a GET")


#####################################################

def post_comment(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        comment_text = request.GET['comment_text']
        # forbidden_words = Forbidden.objects.all()
        #
        # for forbidden_word in forbidden_words:
        #     comment_text = comment_text.replace(forbidden_word.word, ("*" * len(forbidden_word.word)))

        comment = Comment(comment_post=post, comment_text=comment_text, comment_user=request.user)
        comment.save()

        return HttpResponseRedirect('/ourblog/post/' + post_id)

    else:
        return HttpResponse("Request method is not a GET")


#####################################################

def subscribe(request, cat_id, user_id):
    new_sub = CategorySubscribtion.objects.create(subscribed_category_id=cat_id, subscribed_user_id=user_id)
    return JsonResponse({'subs': True}, safe=False)

#####################################################

def unsubscribe(request, cat_id, user_id):
    un_sub = CategorySubscribtion.objects.get(subscribed_category_id=cat_id, subscribed_user_id=user_id)
    un_sub.delete()
    return JsonResponse({'unsubs': True}, safe=False)


#####################################################

def like_view(request,post_id):
    pid=Post.objects.get(id=post_id)
    Like.objects.create(like_post=pid,like_user=request.user)
    return JsonResponse({"state":True,"safe":False})


#####################################################

def unlike_view(request,post_id):
    pid=Post.objects.get(id=post_id)
    Like.objects.filter(like_post=pid,like_user=request.user).delete()
    return JsonResponse({"state": True, "safe": False})


#####################################################

def dislike_view(request,post_id):
    pid=Post.objects.get(id=post_id)
    Dislike.objects.create(dislike_user=request.user,dislike_post=pid)
    count = Dislike.objects.all().count()
    print count
    if count == 10:
        Post.objects.get(id=post_id).delete()
    return JsonResponse({"state": True, "safe": False})


#####################################################


def undislike_view(request,post_id):
    pid=Post.objects.get(id=post_id)
    Dislike.objects.filter(dislike_user_id=request.user,dislike_post_id=pid).delete()
    return JsonResponse({"state": True, "safe": False})


#####################################################


def search_view(request,searchengine):
        result = Post.objects.filter(post_title__contains=searchengine)
        return JsonResponse(serializers.serialize('json',result),safe=False)

#####################################################

# def error_404(request):
#     return render(request, "error404.html")

#####################################################

def is_supped(request,cat_id):
    try:
        CategorySubscribtion.objects.get(subscribed_user=request.user,
                                         subscribed_category=Category.objects.get(id=cat_id))
        return True
    except:
        return False


#####################################################

def is_liked(request, post_id):
    try:
        Like.objects.get(like_user=request.user, like_post=Post.objects.get(id=post_id))
        return True
    except:
        return False

#####################################################

def is_disliked(request, post_id):
    try:
        Dislike.objects.get(dislike_user=request.user,
                                         dislike_post=Post.objects.get(id=post_id))
        return True
    except:
        return False

#####################################################
