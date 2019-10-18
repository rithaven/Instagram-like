from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUploadForm,CommentForm,ProfileForm
from django.http import HttpResponse
from .models import Image,Profile,Likes,Follow,Comment,Unfollow
from django.conf import settings


# Home page view function

@login_required(login_url='/accounts/login')
def Welcome(request):
    title= 'instagram'
    image_posts= Image.objects.all()

    print(image_posts)
    return render(request,'welcome.html',{"title":title,"image_posts":image_posts})


#comment page view function
@login_required(login_url='/accounts/login/')
def comment(request,id):
   
   post = get_object_or_404(Image,id=id)
   current_user= request.user
   print(post)
   if request.method == 'Post':
        from= CommentForm(request.Post)
        if form.is_valid():
               comment = form.save(commit = False)
               comment.user = current_user
               comment.save()
               return redirect('index')
        else:
               form = CommentForm()
        return render(request,'comment.html',{"form":form})

#profile page view function
@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()
    follower = Follow.objects.filter(user = profile)

    return render(request,'userprofile.html',{"current_user":current_user,"profile":profile,"follower":follower})


#timeline page view function
@login_required(login_url='/accounts/login')
def timeline(request):
       current_user = request.user
       theprofile = Profile.objects.order_by('-time_uploaded')
       comment = comment.objects.order_by('-time_comment')

#Single image page view function
@login_required(login_url='/accounts/login')



       return render(request,'all-inst/timeline.html',{"theprofile":theprofile,"comment":comment})

