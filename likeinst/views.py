from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUploadForm,CommentForm,ProfileForm
from django.http import HttpResponse
from .models import Image,Profile,Likes,Follow,Comment
from django.conf import settings


# Home page view function

@login_required(login_url='/accounts/login')
def welcome(request):
    title= 'instagram'
    image_posts= Image.objects.all()

    print(image_posts)
    return render(request,'display/welcome.html',{"title":title,"image_posts":image_posts})


#comment page view function
@login_required(login_url='/accounts/login/')
def comment(request,id):
   
   post = get_object_or_404(Image,id=id)
   current_user= request.user
   print(post)
   if request.method == 'Post':
        form =CommentForm(request.Post)
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

       return render(request,'all-inst/timeline.html',{"theprofile":theprofile,"comment":comment})

#Single image page view function
@login_required(login_url='/accounts/login')
def single_image(request,image_id):
       image = Image.objects.get( id= image_id)

       return render(request, 'display/single_pic.html',{"image":image})

#upvote page view function
@login_required(login_url='/accounts/login')
def upvote(request,image_id):
       Imge = Image.objects.get(id=image_id)
       like +=1
       save_like()
       return redirect(timeline)

#search user page view function
def search_results(request):
       if 'image' in request.GET and request.GET["image"]:
              search_input= request.GET.get("image")
              searched_profiles= Profile.searched_profile(search_input)
              message = f"{search_input}"

              return render (request, 'display/search_pic.html',{"message":message,"images":searched_profiles})

       else:
              message: "you haven't searched for any term"
              return render(request, '/dispaly/search_pic.html',{"message":message})

#upload_profile function to upload profile picture
@login_required(login_url ='/accounts/login')
def upload_profile(request):
    current_user = request.user
    title = 'Upload Profile'
    try:
       requested_prof= Profile.objects.get(user_id= current_user.id)
       if request.method == 'POST':
           form = ProfileUploadForm(request.POST,request.FILES)

           if form.is_valid():
               requested_prof.profile_pic = form.cleaned_data['profile_pic']
               requested_prof.bio = form.cleaned_data['bio']
               requested_prof.username = form.cleaned_data['username']
               requested_prof.save_profile()
               return redirect(profile)

       else:
           form = ProfileUploadForm()

    except:
           if request.method == 'POST':
               form = ProfileUploadForm(request.POST,request.FILES)


               if form .is_valid():
                   new_prof =Profile(profile_pic = form.cleaned_data['profile_pic'], bio= form.cleaned_data['bio'],username= form.cleaned_data['username'])
                   new_prof.save_profile()
                   return redirect(profile)

           else:
              form = ProfileUploadForm()

    return render(request,'display/upload_profpic.html', {"title":title,"current_user":current_user,"form":form})

#send function that will allow user to fill in the form to upload images
@login_required(login_url='/accounts/login')
def send(request):
    '''
    View function that display a form that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

         form = ImageForm(request.POST, request.FILES)

         if form.is_valid():
              pic = form.save(commit = False)
              pic.user_key = current_user

              pic.likes +=0
              pic.save()
              return redirect(timeline)
    else:
           form =ImageForm()

    return render(request,'dispaly/forward.html',{"form":form})


           






       

