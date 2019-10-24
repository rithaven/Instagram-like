from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Image(models.Model):
    '''
     This is a Image model to represent Image table whithin the database
    '''
    image = models.ImageField(upload_to ="photos/",null = True)
    user = models.ForeignKey(User,null = True)
    image_name = models.CharField(max_length =30, null= True)
    votes = models.IntegerField(default = 0)
    image_caption = models.TextField( null = True)
    pub_date = models.DateTimeField(auto_now_add = True, null =True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.pic_name

    def delete_image(self):
        self.delete()
    def save_image(self):
        self.save()
    def update_caption(self,new_caption):
        self.image_caption = new_caption
        self.save()

    @classmethod
    def get_images_by_user(cls,id):
        share_images = Image.objects.filter(user_id=id)
        return share_images

    @classmethod
    def get_images_by_id(cls,id):
        retrieved_image = Image.objects.get(id = id)
        return retrieved_image
    class Meta:
        ordering = ['-pub_date']
    
    def __str__(self):
        return self.image_name

    def save_profile(self):
        self.save()

#########################################################################################################################


class Profile(models.Model):
    '''
     This is a Image model to represent Profile table whithin the database
    '''
    username = models.CharField(default = 'User', max_length=30)
    profile_pic = models.ImageField(upload_to = "profile/",null=True)
    bio = models.TextField(default= '', blank = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.username

    def delete_profile(self):
        self.delete()
    def save_profile(self):
        self.save()
    @classmethod
    def update_profile(cls,id,value):
        cls.objects.filter(id=id).update(user_id= new_user)
    @classmethod
    def searched_profile(cls,search_input):
        found_profile = cls.objects.filter(first_name__icontains =search_input)
        return found_profile

############################################################################################################################

class Comment(models.Model):
    user = models.ForeignKey(User, null = True)
    image = models.ForeignKey(Image, null=True,related_name='comment')
    comment= models.TextField(blank=True)

    def __str__(self):
            return self.comment

    def delete_comment(self):
            self.delete()

    def save_comment(self):
            self.save()

############################################################################################################################

class Follow(models.Model):
    '''
     This is a Image model to represent Follow table whithin the database
    '''
    user = models.ForeignKey(Profile,null=True)
    follower= models.ForeignKey(User,null=True)

    def __int__(self):
        return self.name

    def save_follower(self):
        self.save()

    def delete_follower(self):
        self.save()
      
############################################################################################################################

class Likes(models.Model):

       user= models.ForeignKey(Profile,null=True)

       def __int__(self):
           return self.name

       def unlike(self):
           self.delete()

       def save_like(self):
           self.save()


     

      
         

  

  
    
