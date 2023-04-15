from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Tag
from .forms import PostForm
from django.contrib.auth.decorators import login_required
#blog views

def post_list(request):
    posts = Post.objects.all().order_by('-date_published')[:10]
    latest = Post.objects.order_by('-date_published')[:4]
    
    return render(request, 'blog/post_list.html', {'latest': latest,'posts': posts,'year':'2023'})

def post_detail(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        if post and post.author == request.user:
            post.delete()
            return redirect('home')
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,'year':'2023'})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # set author to the current user
            if not request.POST['introduction']:
                post.introduction = request.POST['content'][:253] + '...'
            post.save()
        return redirect('home')
    else:
        form = PostForm()
        tag_list = Tag.objects.all()
        return render(request,'blog/post_maker.html',{'title':'Create Post','year':'2023','form':form,'tags':tag_list})



    