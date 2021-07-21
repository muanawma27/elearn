from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.
GENDER =(('1','Male'),('2','Female'))
location_pros_cons=[('Healthcare and Medicines',
                    (('Hospital','Hospital'),('Medicine','Medicine'))),
('Industrial and Agri',
    (('Farming','Farming'),('Fishing','Fishing')))]

class LocationChoices(models.Model):
    choice = models.CharField(max_length=200,unique=True,choices=location_pros_cons)

    def __str__(self):
        return self.choice

class IkigaiCategory(models.Model):
    name = models.CharField(max_length=200,unique=True,null=True)

    def __str__(self):
        return self.name
    

class Ikigais(models.Model):
    name = models.CharField(max_length=200,unique=True,null=True)
    category = models.ForeignKey(IkigaiCategory,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class UserIkigai(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

# PROFESSION
    professsion_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P I 1 +")
    profession_ikigai1_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P I 2 +")
    profession_ikigai2_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P I 3 +")
    profession_ikigai3_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P I 4 +")
    profession_ikigai4_value = models.IntegerField(null=True,default=0)
    
    professsion_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="P I 5 +")
    profession_ikigai5_value = models.IntegerField(null=True,default=0)

# INTEREST
    interest_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I I 1 +")
    interest_ikigai1_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I I 2 +")
    interest_ikigai2_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I I 3 +")
    interest_ikigai3_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I I 4 +")
    interest_ikigai4_value = models.IntegerField(null=True,default=0)
    
    interest_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="I I 5 +")
    interest_ikigai5_value = models.IntegerField(null=True,default=0)

# HOBBY 
    hobby_ikigai1 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H I 1 +")
    hobby_ikigai1_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai2 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H I 2 +")
    hobby_ikigai2_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai3 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H I 3 +")
    hobby_ikigai3_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai4 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H I 4 +")
    hobby_ikigai4_value = models.IntegerField(null=True,default=0)
    
    hobby_ikigai5 = models.ForeignKey(Ikigais,on_delete=models.CASCADE,null=True,blank=True,related_name="H I 5 +")
    hobby_ikigai5_value = models.IntegerField(null=True,default=0)

    def __str__(self):
        return self.user.username
    


class Location(models.Model):
    name = models.CharField(max_length=200,unique=True)
    goods = models.ManyToManyField(LocationChoices)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    age = models.IntegerField(null=True)
    address = models.ForeignKey(Location,null=True,on_delete=models.CASCADE)
    gender = models.CharField(max_length=200,null=True,choices=GENDER)
    profilephoto = models.ImageField(upload_to = 'profilephoto/',null=True,blank=True,default='default.jpg')
    def __str__(self):
        return self.user.username

class Interests():
    pass
    # Five interest types

class Hobby():
    pass
    #Five hobby types

class Profession():
    pass
    #profession
    # level

class Goal():
    pass

class SkillSets(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    profession = models.IntegerField(default=0)
    hobbies = models.IntegerField(default=0)
    interests = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    