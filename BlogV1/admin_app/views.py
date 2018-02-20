from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from posts_app.models import Post , Category
from forms import PostForm , CategoryForm

def allposts(request):
   all_posts = Post.objects.all()
   context={
       "allposts":all_posts
   }
   return render(request,'allposts.html',context)
################################################
def post_create(request):
    form=PostForm()
    if request.method=="POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("allposts")
    context={
        "form":form,
    }
    return render(request,"post_form.html",context)
##################################################
def post_retrive(request , post_id):
    obj=Post.objects.get(id=post_id)
    context={
        "obj": obj,
    }
    return render(request,"post_detail.html",context)
######################################################
def post_update(request,post_id):
    obj = Post.objects.get(id=post_id)
    #return HttpResponse(obj)
    form = PostForm(instance=obj)

    if request.method == "POST":
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/allposts')

    context={
        "form":form
    }
    return render(request,'post_form.html',context)
###############################################
def post_delete(request , post_id):
    obj=Post.objects.get(id=post_id)
    obj.delete()
    return HttpResponseRedirect('/admin/allposts')

################################################
################################################

def allcategory(request):
    all_category=Category.objects.all()
    context={
        "allcategory":all_category
    }
    return render(request,'allcategory.html',context)
#####################################################
def category_create(request):
    category_form=CategoryForm()
    if request.method=="POST":
        category_form= CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("allcategory")
    context={
        "category_form":category_form,
    }
    return render(request,'category_form.html',context)
##########################################################
def category_retrive(request , category_id):
    obj=Category.objects.get(id=category_id)
    context={
        "obj":obj,
    }
    return render(request,'category_detail.html',context)
###########################################################
def category_update(request,category_id):
    obj=Category.objects.get(id=category_id)
    form=CategoryForm(instance=obj)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/allcategory')
    context={
        "form":form
    }
    return render(request,'category_form.html',context)
###############################################################
def category_delete(request , category_id):
    obj=Category.objects.get(id=category_id)
    obj.delete()
    return HttpResponseRedirect('allcategory')
###########################################################