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
        form = PostForm(request.POST)
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
    return render(request,"post_form.html",context)
###############################################
def post_delete(request , post_id):
    obj=Post.objects.get(id=post_id)
    return HttpResponseRedirect('/admin/allposts')

###############################################


# def new_user(request):
# 	user_form=StudentForm()
# 	if request.method=="POST":
#         user_form=StudentForm(request.POST)
# 		if user_form.is_valid():
# 			user_form.save()
# 			return HttpResponseRedirect("")
#
# 	context={"form":user_form}
# 	return render(request,"student/new.html",context)