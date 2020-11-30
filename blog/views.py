from django.shortcuts import render,redirect
from .models import Post
import re
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse

def openEditor(request):
    return render(request,"editor.html")

def addList(request):
    if request.method=='GET':
        return redirect("home")
    
    title=request.POST["tit"]
    cont=request.POST["text"]
    cont=cont.replace('&lt;','<')
    cont=cont.replace('&gt;','>')
    cont=cont.replace('&nbsp;',' ')

    form = request.FILES["pic"]
    obj=Post(title=title,content=cont,image=form)
    obj.save()

    return redirect("home")

def PostList(request):
    #fetch page no
    page = request.GET.get('page', 1)

    blogs=Post.objects.order_by('-created_on')

    #On a single page there will be 4 blogs 
    paginator = Paginator(blogs, 4)
    return render(request,"index.html",{"post_list":paginator.page(page)})

def PostDetail(request,blog_id):
    ob=Post.objects.get(pk=blog_id)
    s=str(ob.image)
    url=request.build_absolute_uri()

    #Add onclick functionality to a
    content=ob.content
    #content=content.replace("<a",'<a ')
    content=content.replace('"',"")

    #new path
    new_path = url[:[m.start() for m in re.finditer(r"/",url)][2]+1]+s[s.index('static'):]

    return render(request,"post_detail.html",{"object":ob,"url":request.build_absolute_uri(),"image_cont":new_path,"cont":content})

def update_like(request,blog_id):
    ob=Post.objects.get(pk=blog_id)
    old_like=ob.likes
    ob.likes=old_like+1
    ob.save()

    response={'like':old_like+1}
    return JsonResponse(response)