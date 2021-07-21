from functools import total_ordering
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

from account.models import Ikigais,IkigaiCategory


 
STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2, "Delete")
)
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200,null=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=500,null=True,blank=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    profession_outcome = models.IntegerField(null=True)
    interest_outcome = models.IntegerField(null=True)
    hobby_outcome = models.IntegerField(null=True)
    courseimage = models.ImageField(upload_to="courseimage/",blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        return super().save(*args,**kwargs)




# creating an django model class
class Post(models.Model):
    # title field uing charfield constraint with unique constraint
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category,null=True,on_delete = models.CASCADE)
    # slug field auto populated using title with unique constraint
    slug = models.SlugField(max_length=200, null=True,blank=True)
    # author field populated using users database
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    # and date time fields automatically populated using system time
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField()
    # content field to store our post
    content = CKEditor5Field('Text', config_name='extends',blank=True)
    # meta descrption for SEO benifits
    metades = models.CharField(max_length=300, default="new post")
    # status of post
    status = models.IntegerField(choices=STATUS, default=0)

    header = models.ForeignKey("self",null=True,on_delete=models.CASCADE,related_name='post_header',blank=True)
    trailing = models.ForeignKey("self",null=True,on_delete=models.CASCADE,related_name='post_trailing',blank=True)

    coverimage = models.ImageField(upload_to ='coverimage',null=True,blank=True,default='/assets/images/favpih.svg')
    tags = models.CharField(max_length=500,null=True)
 
    # meta for the class
    class Meta:
        ordering = ['-created_on']
    # used while managing models from terminal
    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)

        if not self.coverimage:
            self.coverimage = '/courseimage/favpih.svg'
        return super().save(*args,**kwargs)


class CourseOrdering(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    content = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    part_no = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.part_no} - {self.content}'

  
 

class UserCourse(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    current_location = models.ForeignKey(CourseOrdering,on_delete=models.CASCADE, null=True)
    completed = models.BooleanField(default=False)
    progress = models.FloatField(default=0,null=True)


    def __str__(self):
        return f'{self.user} - {self.course}'
class UserCourseActivity(models.Model):
    usercourse = models.ForeignKey(UserCourse,on_delete=models.CASCADE,null=True)
    completed_listing = models.TextField(blank=True)

class Ratings(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    
    def __str__(self):
        return f'{self.user} - {self.post} - {self.rating}'

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    review = models.CharField(null=True,max_length=800)

    
    def __str__(self):
        return f'{self.user} - {self.post} - {self.review}'

class CourseIkigai(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

# PROFESSION
    professsion_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P C 1 +")
    profession_ikigai1_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P C 2 +")
    profession_ikigai2_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P C 3 +")
    profession_ikigai3_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P C 4 +")
    profession_ikigai4_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P C 5 +")
    profession_ikigai5_value = models.IntegerField(null=True,default=0)

# INTEREST
    interest_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I C 1 +")
    interest_ikigai1_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I C 2 +")
    interst_ikigai2_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I C 3 +")
    interest_ikigai3_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I C 4 +")
    interest_ikigai4_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I C 5 +")
    interest_ikigai5_value = models.IntegerField(null=True,default=0)

# HOBBY 
    hobby_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H C 1 +")
    hobby_ikigai1_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H C 2 +")
    hobby_ikigai2_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H C 3 +")
    hobby_ikigai3_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H C 4 +")
    hobby_ikigai4_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H C 5 +")
    hobby_ikigai5_value = models.IntegerField(null=True,default=0)


    def __str__(self):
        return self.course.name


    
class Transactions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}-{self.course}'
    