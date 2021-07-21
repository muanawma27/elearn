# importing django routing libraries
from . import views
from django.urls import path, include
from .views import *
# from .feeds import blogFeed

urlpatterns = [
	# home page
	path('', views.postlist, name='postlist'),
	path('explore', views.explore, name='explore'),

	# route for posts
	# path('<slug:slug>/', views.Postdetail.as_view(), name='postdetail'),
	path('detail/<slug:slug>/', views.postdetail, name='postdetail'),

	path('rate/<slug:slug>/<int:values>', views.rate, name='rate'),



	path('courses/', views.courselist, name='courselist'),
	path('info/<slug:slug>/', views.courseinfo, name='courseinfo'),
	path('course/<slug:slug>/<int:id>',views.coursedetail,name='coursedetail'),

	path('courses/<str:course>',views.takecourse,name='takecourse'),
	path('courses/<str:course>/<int:id>',views.usercourseupdate,name='usercourseupdate'),


	path('courses/<str:course>/activity/<int:part_no>',views.usercourseactivity,name='usercourseactivity'),




	



]
