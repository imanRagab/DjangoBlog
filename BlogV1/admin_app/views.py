from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

import time

import os
from admin_app.forms import PostForm, CategoryForm, TagForm, ForbiddenForm, UploadFileForm
from posts_app.forms import UserRegForm
from posts_app.models import Category, CategorySubscribtion, Post, Tag,Comment, Reply, Like, Dislike, Forbidden
from django.contrib.auth.models import User

def dashboard(request):
    if (request.user.is_staff):
        return render(request, 'admin/dashboard.html')

    else:
        return HttpResponseRedirect('/ourblog/login/')

########################################

def all(request, model):

    if(request.user.is_staff):

        if(model == "category"):
            objects = Category.objects.all()

        elif(model == "post"):
            objects = Post.objects.all()

        elif (model == "tag"):
            objects = Tag.objects.all()

        elif(model == "comment"):
            objects = Comment.objects.all()

        elif (model == "reply"):
            objects = Reply.objects.all()

        elif (model == "like"):
            objects = Like.objects.all()

        elif (model == "dislike"):
            objects = Dislike.objects.all()

        elif (model == "forbidden"):
            objects = Forbidden.objects.all()

        elif (model == "subscription"):
            objects = CategorySubscribtion.objects.all()


        elif (model == "user"):
            objects = User.objects.all()

        paginator = Paginator(objects, 10)  # Show 10 elements per page
        if request.GET.get('page'):
            page = request.GET.get('page')
        else:
            page = 1
        page_objects = paginator.page(page)
        context = {'objects': page_objects, 'model': model}

        return render(request, 'admin/all.html', context)

    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################

def add(request, model):

    if(model == "category"):
        form = CategoryForm(request.POST)

    elif(model == "post"):
        form = PostForm(request.POST, request.FILES or None)
        # file_form = UploadFileForm(request.POST, request.FILES)

    elif (model == "forbidden"):
        form = ForbiddenForm(request.POST)

    elif (model == "user"):
        form = UserRegForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            # if file_form.is_valid():
            #     file_dir = os.path.dirname(os.path.realpath('__file__'))
            #     rel_path = "BlogV1/posts_app/static/images/posts_images" + time.time()
            #     abs_file_path = os.path.join(file_dir, rel_path)
            #     with open(abs_file_path, 'wb+') as destination:
            #         for chunk in request.FILES['file'].chunks():
            #             destination.write(chunk)

            return HttpResponseRedirect('/ourblog/admin/all/' + model)

    context = {"form": form, 'model': model}

    return render(request, 'admin/add.html', context)


##########################################################

def edit(request, model, object_id):

    if (model == "category"):
        object = Category.objects.get(id=object_id)
        form = CategoryForm(request.POST or None, instance=object)

    elif (model == "post"):
        object = Post.objects.get(id=object_id)
        form = PostForm(request.POST or None, instance=object)

    elif (model == "forbidden"):
        object = Forbidden.objects.get(id=object_id)
        form = ForbiddenForm(request.POST or None, instance=object)

    elif (model == "user"):
        object = User.objects.get(id=object_id)
        form = UserRegForm(request.POST or None, instance=object)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ourblog/admin/all/' + model)

    context = {"form": form, 'model': model, 'object_id': object_id}

    return render(request, 'admin/edit.html', context)


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


#########################################################

# def error_404(request):
#     return render(request, "error404")