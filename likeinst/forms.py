from django import forms
from .models import Comment,Profile,Image
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
      model = Profile
      username = forms.CharField(label='Username',max_length=30)

      bio=forms.CharField(label='Image Caption',max_length=500)
      profile_pic=forms.ImageField(label= 'Image Field')

class ProfileUploadForm(forms.ModelForm):
        class Meta:
                modal = Profile

                exclude = ['user']

class CommentForm(forms.ModelForm):
        class Meta:
              model = Comment

              exclude = ['user','image']