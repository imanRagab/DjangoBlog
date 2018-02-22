from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
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

def allposts(request):
   all_posts = Post.objects.all()
   context={
       "allposts":all_posts
   }
   return render(request,'admin/allposts.html',context)
################################################
def post_create(request):
    form=PostForm()
    if request.method=="POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/ourblog/admin/allposts")
    context={
        "form":form,
    }
    return render(request,"admin/post_form.html",context)
##################################################
def post_retrive(request , post_id):
    obj=Post.objects.get(id=post_id)
    context={
        "obj": obj,
    }
    return render(request,"admin/post_detail.html",context)
######################################################
def post_update(request,post_id):
    obj = Post.objects.get(id=post_id)
    #return HttpResponse(obj)
    form = PostForm(instance=obj)

    if request.method == "POST":
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ourblog/admin/allposts')

    context={
        "form":form
    }
    return render(request,'admin/post_update.html',context)
###############################################
def post_delete(request , post_id):
    obj=Post.objects.get(id=post_id)
    obj.delete()
    return HttpResponseRedirect('/ourblog/admin/allposts')

################################################
################################################

def allcategory(request):
    all_category=Category.objects.all()
    context={
        "allcategory":all_category
    }
    return render(request,'admin/allcategory.html',context)
#####################################################
def category_create(request):
    category_form=CategoryForm()
    if request.method=="POST":
        category_form= CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/ourblog/admin/allcategory")
    context={
        "form":category_form,
    }
    return render(request,'admin/category_form.html',context)
##########################################################
def category_retrive(request , category_id):
    obj=Category.objects.get(id=category_id)
    context={
        "obj":obj,
    }
    return render(request,'admin/category_detail.html',context)
###########################################################
def category_update(request,category_id):
    obj=Category.objects.get(id=category_id)
    form=CategoryForm(instance=obj)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ourblog/admin/allcategory')
    context={
        "form":form
    }
    return render(request,'admin/category_update.html',context)
###############################################################
def category_delete(request , category_id):
    obj=Category.objects.get(id=category_id)
    obj.delete()
    return HttpResponseRedirect('/ourblog/admin/allcategory')
###########################################################

########################################

def all(request, model):

    if(request.user.is_staff):


        if (model == "tag"):
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

        if (model == "forbidden"):
            form = ForbiddenForm(request.POST)

        elif (model == "user"):
            form = UserRegForm(request.POST)

        elif (model == "tag"):
            form = TagForm(request.POST)

        if form:
            if request.method == "POST":
                if form.is_valid():
                    form.save()

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


            if (model == "forbidden"):
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
                    form.save()
                    return HttpResponseRedirect('/ourblog/admin/all/' + model)

            context = {"form": form, 'model': model, 'object_id': object_id}
            return render(request, 'admin/edit.html', context)

    else:
        return HttpResponseRedirect('/ourblog/login/')


##########################################################

def delete(request, model, object_id):

    if (request.user.is_staff):

        try:

            if (model == "forbidden"):
                forbidden_word = Forbidden.objects.get(id=object_id)
                forbidden_word.delete()

            else:
                raise Http404("Post does not exist")

        except:
            raise Http404("Post does not exist")

        return redirect(request.META['HTTP_REFERER'])

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