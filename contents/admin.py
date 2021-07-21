from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(CourseOrdering)
admin.site.register(UserCourse)
admin.site.register(Ratings)
admin.site.register(Review)
admin.site.register(CourseIkigai)
admin.site.register(UserCourseActivity)
admin.site.register(Transactions)






