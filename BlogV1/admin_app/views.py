from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from posts_app.forms import UserRegForm, ReplyForm, CommentForm
from posts_app.models import Category, CategorySubscribtion, Post, Tag,Comment, Reply, Like, Dislike, Forbidden
from django.contrib.auth.models import User

def dashboard(request):
    return render(request, 'admin/dashboard.html')


########################################

def all(request, model):
    context = {}
    if(model == "category"):
        categories = Category.objects.all()
        context = {'objects': categories, 'model': model}

    elif(model == "post"):
        posts = Post.objects.all()
        context = {'objects' : posts,'model': model}

    elif (model == "tag"):
        tags = Tag.objects.all()
        context = {'objects': tags,'model': model}

    elif(model == "comment"):
        comments = Comment.objects.all()
        context = {'objects' : comments,'model': model}

    elif (model == "reply"):
        replies = Reply.objects.all()
        context = {'objects': replies,'model': model}

    elif (model == "like"):
        likes = Like.objects.all()
        context = {'objects': likes,'model': model}

    elif (model == "dislike"):
        dislikes = Dislike.objects.all()
        context = {'objects': dislikes,'model': model}

    elif (model == "forbidden"):
        forbidden_words = Forbidden.objects.all()
        context = {'objects': forbidden_words,'model': model}

    elif (model == "subscription"):
        subscriptions = CategorySubscribtion.objects.all()
        context = {'objects': subscriptions,'model': model}

    elif (model == "user"):
        users = User.objects.all()
        context = {'objects': users,'model': model}

    return render(request, 'admin/all.html', context)


#########################################################

def add(request, model):
    if(model == "category"):
        category_form = Category.objects.all()
        context = {'form': category_form}
        return render(request, 'admin/add.html', context)

    elif(model == "post"):
        post_form = Post.objects.all()
        context = {'form' : post_form}
        return render(request, 'admin/add.html', context)


    elif (model == "forbidden"):
        forbidden_word_form = Forbidden.objects.all()
        context = {'form': forbidden_word_form}
        return render(request, 'admin/add.html', context)

    elif (model == "user"):
        user_form = UserRegForm()
        context = {'form': user_form}
        return render(request, 'admin/add.html', context)


##########################################################

def edit(request, model, object_id):
    if(model == "category"):
        category_form = Category.objects.all()
        context = {'form': category_form}
        return render(request, 'admin/add.html', context)

    elif(model == "post"):
        post_form = Post.objects.all()
        context = {'form' : post_form}
        return render(request, 'admin/add.html', context)


    elif (model == "forbidden"):
        forbidden_word_form = Forbidden.objects.all()
        context = {'form': forbidden_word_form}
        return render(request, 'admin/add.html', context)

    elif (model == "user"):
        user_form = UserRegForm()
        context = {'form': user_form}
        return render(request, 'admin/add.html', context)


##########################################################

def delete(request, model, object_id):
    if (model == "category"):
        category = Category.objects.get(id=object_id)
        category.delete()

    elif (model == "post"):
        post = Post.objects.get(id=object_id)
        post.delete()

    elif (model == "forbiddenword"):
        forbidden_word = Forbidden.objects.get(id=object_id)
        forbidden_word.delete()

    return redirect(request.META['HTTP_REFERER'])

#########################################################

def block_user(request, user_id):

    user = User.objects.get(id=user_id)
    user.is_active = 0
    user.save()

    return redirect(request.META['HTTP_REFERER'])

#########################################################

def unblock_user(request, user_id):

    user = User.objects.get(id=user_id)
    user.is_active = 1
    user.save()

    return redirect(request.META['HTTP_REFERER'])

#########################################################

def make_admin(request, user_id):

    user = User.objects.get(id=user_id)
    user.is_staff = 1
    user.save()

    return redirect(request.META['HTTP_REFERER'])