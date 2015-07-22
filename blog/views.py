from django.shortcuts import render,get_object_or_404
from .models import Post
from django.utils import timezone
def post_list(request):
	post=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
	return  render(request,'blog/post_list.html',{'posts':post})

def post_details(request,pid):
	post=get_object_or_404(Post,pk=pid)
	return render(request,'blog/post_details.html',{'post':post})