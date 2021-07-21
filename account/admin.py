from django.contrib import admin
from .models import *
# Register your models here.
models_registered = [Location,LocationChoices,Profile,IkigaiCategory,Ikigais,UserIkigai,SkillSets]
admin.site.register(models_registered)