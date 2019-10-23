from django.test import TestCase
from .models import Profile,Comment,Image
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestclass(TestCase):
     #setup method
     def setUp(self):
       self.username = User.objects.create(id=1,username= 'ritha')
       self.profile = Profile(first_name ='nina',last_name ='bella',profile_pic = 'g.jpeg',bio ='fine',username = self.username)

     def test_instance(self):
         self.assertTrue(isinstance(self.profile,Profile))
     def test_save_method(self):
         self.profile.save_profile()
         self.profile.delete_profile()
         profile = Profile.objects.all()
         self.assertTrue(len(profile)>=0)

     def test_update_method(self):
         self.profile.save_profile()
         new_prof = Profile.objects.filter(bio ='fine').update(bio ='coool')
         
class CommentTestClass(TestCase):
   #setup method
   def setUp(self):
       self.comment= Comment.objects.create(comment ='very nice')
   def test_instance(self):
       self.comment.save_comment()
       comment =Comment.objects.all()
       self.assertTrue(len(comment)>0)

   def test_delete_method(self):
       self.comment.save_comment()
       self.comment.delete_comment()
       comment = Comment.objects.all()
       self.assertTrue(len(comment)>=0)

class ImageTestClass(TestCase):

  #setup method
   def setUp(self):
       self.image =Image(image ='ken.jpg',image_name='test',image_caption ='This is a google image') 
   def tearDown(self):
       Image.objects.all().delete()
       Profile.objects.all().delete()

   def test_instance(self):
       self.assertTrue(isinstance(self.image,Image))

   def test_save_method(self):
       self.image = Image (image ='hf.jpg', image_name='test',image_caption='this is a google image')
       self.image.save_image()
       images = Image.objects.all()
       self.assertTrue(len(images)>=1)

   def test_delete_method(self):
       self.image = Image (image ='hf.jpg', image_name='test',image_caption='this is a google image')
       self.image.save_image()
       images = self.image.delete_image()
       delete = Image.objects.all()
       self.assertTrue(len(delete)<=0)
     
    