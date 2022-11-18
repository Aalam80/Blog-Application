from urllib import request
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import BlogPostForm,Userregistrationform
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def Post_list(request):
    response_data = Post.objects.all()
    # return HttpResponse(response_data)
    return render(request,'Blog/index.html',{'Posts':response_data })

def post_details_page (request,pk):
    Post_data= get_object_or_404 (Post,pk=pk)
    # return HttpResponse(Post_data)
    return render (request,'Blog/blog_detail.html',{'data': Post_data})


@login_required
def Post_new(request):
    if request.method=='POST':
        form_data =BlogPostForm (request.POST)#capturing form data
        if form_data.is_valid():
            Post_data=form_data.save()
            return redirect('Post_list')#redirect to the post_list
    else:
        form_data=BlogPostForm()
    return render(request,'Blog/blog_add_edit.html',{'form_data':form_data})
       


def Post_edit(request,pk):
    Post_data= get_object_or_404 (Post,pk=pk)
    if request.method=='POST':
        form =BlogPostForm (request.POST,instance=Post_data)#capturing form data
        if form.is_valid():
            Post_data=form.save()
            return redirect('Post_list')#redirect to the post_list3
            
    else:
        form=BlogPostForm(instance=Post_data)
    return render(request,'Blog/blog_add_edit.html',{'form_data':form})
       
    

def Post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('Post_list')


    
def register_user(request):
    if request.method=='POST':
        form =Userregistrationform (request.POST)#capturing form data
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account create succsefully for {username}')
            return redirect('Post_list')

    else:
        form= Userregistrationform ()
    return render(request,'registration/register.html',{'form': form})

