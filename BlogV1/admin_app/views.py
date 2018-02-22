from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect

# import time
#
# import os
from admin_app.forms import PostForm, CategoryForm, TagForm, ForbiddenForm
from auth_app.forms import UserRegForm
from posts_app.models import Category, CategorySubscribtion, Post, Tag,Comment, Reply, Like, Dislike, Forbidden, PostsTags
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

        if object:
            paginator = Paginator(objects, 10)  # Show 10 elements per page
            if request.GET.get('page'):
                page = request.GET.get('page')
            else:
                page = 1
            page_objects = paginator.page(page)
            context = {'objects': page_objects, 'model': model}

            return render(request, 'admin/all.html', context)

        else:
            raise Http404("Page does not exist")

    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################
def add(request, model):

    if (request.user.is_staff):

        if(model == "category"):
            form = CategoryForm(request.POST)

        elif(model == "post"):
            form = PostForm(request.POST, request.FILES or None)
            # file_form = UploadFileForm(request.POST, request.FILES)

        elif (model == "forbidden"):
            form = ForbiddenForm(request.POST)

        elif (model == "user"):
            form = UserRegForm(request.POST)

        elif (model == "tag"):
            form = TagForm(request.POST)

        if form:
            if request.method == "POST":
                if form.is_valid():
                    obj = form.save()
                    if model == "post":
                        tags = request.POST.get('post_tags')
                        for tag in tags:
                            tagObj = Tag.objects.create(tag_name=tag)
                            PostsTags.objects.create(post=obj, tag=tagObj)

                    return HttpResponseRedirect('/ourblog/admin/all/' + model)

            context = {"form": form, 'model': model}

            return render(request, 'admin/add.html', context)

        else:
            raise Http404("Page does not exist")

    else:
        return HttpResponseRedirect('/ourblog/login/')


##########################################################

def edit(request, model, object_id):

    if (request.user.is_staff):

            if (model == "category"):
                try:
                    object = Category.objects.get(id=object_id)
                except:
                    raise Http404("Post does not exist")
                form = CategoryForm(request.POST or None, instance=object)

            elif (model == "post"):
                try:
                    object = Post.objects.get(id=object_id)
                except:
                    raise Http404("Post does not exist")
                form = PostForm(request.POST or None, instance=object)

            elif (model == "forbidden"):
                try:
                    object = Forbidden.objects.get(id=object_id)
                except:
                    raise Http404("Post does not exist")
                form = ForbiddenForm(request.POST or None, instance=object)

            elif (model == "user"):
                try:
                    object = User.objects.get(id=object_id)
                except:
                    raise Http404("Post does not exist")
                form = UserRegForm(request.POST or None, instance=object)

            else:
                raise Http404("Post does not exist")


            if request.method == "POST":
                if form.is_valid():
                    obj = form.save()
                    if model == "post":
                        tags = request.POST.get('post_tags')
                        for tag in tags:
                            tagObj = Tag.objects.get(tag_name=tag)
                            PostsTags.objects.create(post=obj, tag=tagObj)

                    return HttpResponseRedirect('/ourblog/admin/all/' + model)

            context = {"form": form, 'model': model, 'object_id': object_id}
            return render(request, 'admin/edit.html', context)

    else:
        return HttpResponseRedirect('/ourblog/login/')


##########################################################

def delete(request, model, object_id):

    if (request.user.is_staff):

        try:

            if (model == "category"):
                category = Category.objects.get(id=object_id)
                category.delete()

            elif (model == "post"):
                post = Post.objects.get(id=object_id)
                post.delete()

            elif (model == "forbidden"):
                forbidden_word = Forbidden.objects.get(id=object_id)
                forbidden_word.delete()

            else:
                raise Http404("Post does not exist")

        except:
            raise Http404("Post does not exist")

        return HttpResponseRedirect('/ourblog/admin/all/' + model)

    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################

def block_user(request, user_id):

    if (request.user.is_staff):

        try:
            user = User.objects.get(id=user_id)
            user.is_active = 0
            user.save()

            return redirect(request.META['HTTP_REFERER'])

        except:
            raise Http404("Post does not exist")

    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################

def unblock_user(request, user_id):

    if (request.user.is_staff):

        try:
            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()

        except:
            raise Http404("Post does not exist")

        return redirect(request.META['HTTP_REFERER'])


    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################

def make_admin(request, user_id):

    if (request.user.is_staff):

        try:
            user = User.objects.get(id=user_id)
            user.is_staff = 1
            user.save()

        except:
            raise Http404("Post does not exist")

        return redirect(request.META['HTTP_REFERER'])


    else:
        return HttpResponseRedirect('/ourblog/login/')


#########################################################

# def error_404(request):
#     return render(request, "error404")
