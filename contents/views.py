from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect


# Create your views here.
# importing models and libraries
from django.shortcuts import render
from numpy import less_equal
from .models import CourseOrdering, Post,Course, Ratings, Transactions,UserCourse, UserCourseActivity
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.contrib.auth.models import User
# class based views for posts
# for MACHINE LEARNING
from .contentbased import recommend
from .postrecommendation import recommendation

# For courser recommendation
from .models import CourseIkigai
from account.models import SkillSets, UserIkigai,Ikigais

def postlist(request):
    
    if request.user.is_authenticated:
        print(request.user.id)

        try:

            post_list = recommendation(userid=request.user.id)
            print(post_list)
            # postlist =Post.objects.filter(status=1).order_by('-created_on')
            postlist =Post.objects.filter(title__in = post_list).order_by('-created_on')
            print(postlist)
            postlist2 = Post.objects.all().exclude(title__in =postlist)
            postlist = postlist|postlist2
            print(postlist)
        except:
            postlist = Post.objects.all()
            return render(request,'postlist.html',{'postlist':postlist})

        
        return render(request,'postlist.html',{'postlist':postlist})

    else:
        return render(request,'base/index.html')

# class based view for each post
# class Postdetail(generic.DetailView):
#     model = Post
#     template_name = "postdetail.html"

def postdetail(request,slug):
    post = Post.objects.get(slug=slug)
    recommend(item_id=post.id, num=5)
    recommendation = recommend(item_id=post.id, num=1)
    recommended = Post.objects.get(title=recommendation)

    user = request.user
    if Ratings.objects.filter(post=post,user=user).exists():
        rating = Ratings.objects.get(post=post,user=request.user)
        ratings = rating.rating
        negativeratings = abs(ratings-5)
    else:
        ratings =0
        negativeratings = 0

 

    return render(request,'postdetail.html',{'object':post,'recommended':recommended,'ratings':range(ratings),'negativeratings':range(negativeratings)})

def courselist(request):
    # courselist = Course.objects.all()
    user = request.user
    user_profession=[]
    user_hobby=[]
    user_interest=[]

    if UserIkigai.objects.filter(user=user).exists():
        p = UserIkigai.objects.get(user=user)
    else:
        p= UserIkigai.objects.create(user=user)
        courselist = Course.objects.all()
    for i in range(5):
        if (i !=0) and (i < 6):
            name = f'professsion_ikigai{i}'
            pvalue = getattr(p,name)
            if pvalue != None:
                # continue
            # else:
                user_profession.append(pvalue)

            name = f'hobby_ikigai{i}'
            pvalue = getattr(p,name)
            if pvalue != None:
                # continue
            # else:
                user_hobby.append(pvalue)

            name = f'interest_ikigai{i}'
            pvalue = getattr(p,name)
            if pvalue != None:
                # continue
            # else:
                user_interest.append(pvalue)

            

    print("USER PROFESSIONS",user_profession)
    print("USER HOBBY",user_hobby)
    print("USER INTEREST",user_interest)



    pc= CourseIkigai.objects.filter(professsion_ikigai1__in=user_profession)
    hc= CourseIkigai.objects.filter(hobby_ikigai1__in=user_hobby)
    ic= CourseIkigai.objects.filter(interest_ikigai1__in=user_interest)
    print("IKIGAI COURSE:",pc,hc,ic)
    ppc = []
    hhc=[]
    iic=[]
    for i in pc:
        ppc.append(i.course)
    for i in hc:
        hhc.append(i.course)
    for i in ic:
        iic.append(i.course)

    print("APPENDED",ppc,hhc,iic)

    courselist1 = Course.objects.filter(name__in =ppc)
    courselist2 = Course.objects.filter(name__in =hhc)
    courselist3 = Course.objects.filter(name__in =iic)
    courselist = courselist1|courselist2|courselist3
    print(courselist)
    # print(pc,hc,ic)
    return render(request,'course/courselist.html',{'courselist':courselist})

def courseinfo(request,slug):
    course = Course.objects.get(slug=slug)
    return render(request,'course/courseinfo.html',{'course':course})

def coursedetail(request,slug,id):
    partno=id
    course = Course.objects.get(slug=slug)
    courselist = CourseOrdering.objects.filter(course=course).order_by('part_no')
    courseorderpost = CourseOrdering.objects.get(course=course, part_no = id)

    usercourse= UserCourse.objects.get(course=course,user=request.user)
    if usercourse.completed == True:
        course_status= 1
    else:
        course_status =0

    post = Post.objects.get(id=courseorderpost.content.id)
    return render(request,'course/coursedetail.html',{'course':course,'courselist':courselist,'post':post,'partno':partno,'course_status':course_status})


def rate(request,slug,values):
    post = Post.objects.get(slug=slug)
    existed,created = Ratings.objects.get_or_create(post=post,user=request.user)
    if created:
        created = Ratings.objects.get(post=post,user=request.user)
        created.rating = values
        created.save()

    else:
        existed = Ratings.objects.get(post=post,user=request.user)
        existed.rating = values
        existed.save()
    return redirect(f'/detail/{slug}/')

def takecourse(request,course):
    user =request.user
    print(course)
    course = Course.objects.get(id=course)
    courseorder = CourseOrdering.objects.get(course=course,part_no=1)

    if UserCourse.objects.filter(course = course,user=user).exists() is False:
        C = UserCourse.objects.create(course = course,user=user,current_location = courseorder)
        # C.current_location = courseorder
        # C.save()
        print("CURRENT",C.current_location)

    else:
        C = UserCourse.objects.get(course = course,user=user)
        C.current_location = courseorder
        C.save()   
    
    return redirect(f'/course/{course.slug}/1')

def usercourseupdate(request,course,id):
    user = request.user
    course = Course.objects.get(slug=course)
    courseorder = CourseOrdering.objects.get(course=course,part_no=id)
    C = UserCourse.objects.get(course=course,user=user)
    # print(courseorder.part_no)
    C.current_location = courseorder
    print(C.current_location)
    C.save()

    return redirect(f'/course/{course.slug}/{courseorder.part_no}')
    
    

def usercourseactivity(request,course,part_no):
    print("course",course)
    user = request.user
    print("part_no",part_no)
    course = Course.objects.get(slug=course)
    usercourse = UserCourse.objects.get(course=course,user=user)
    # Current course
    courseorder = CourseOrdering.objects.get(course=course,part_no=part_no)
    usercourse.current_location = courseorder
    # course completed list
    UserCourseActivity.objects.get_or_create(usercourse=usercourse)
    usercourseactivity = UserCourseActivity.objects.get(usercourse=usercourse)

    comp_list=[]
    comp_list.append(part_no)

    for i in list(usercourseactivity.completed_listing):
        if i.isnumeric() and i not in comp_list:
            comp_list.append(i)
    usercourseactivity.completed_listing = comp_list
    usercourseactivity.save()
    print(usercourseactivity.completed_listing)

    # getting course list
    count =0 
    count2 =0
    courseorder = CourseOrdering.objects.filter(course=course)
    for i in courseorder:
        count +=1
    for i in comp_list:
        count2 +=1
    count2 =count2 -1
    print("Course total",count)
    print("Completed",count2)
    completion_percentage = (float(count2))/(float(count))*100
    usercourse.progress=completion_percentage
    print("Progress Percentage:",completion_percentage)
    if completion_percentage >= 99.0:
        usercourse.completed =True
        usercourse.save()
        if Transactions.objects.filter(user=user,course=course).exists():
            pass
        else:
            t=Transactions.objects.create(user=user,course=course)
            usersskillset,usercreate = SkillSets.objects.get_or_create(user=user)
            usersskillset.profession = course.profession_outcome + usersskillset.profession
            usersskillset.hobbies = course.hobby_outcome + usersskillset.hobbies
            usersskillset.interests = course.interest_outcome + usersskillset.interests

            usersskillset.save()
            print(usersskillset.profession,usercreate)
        user = User.objects.get(username=request.user)
        certificate_id = f'{user.id}{str(course)[:3]}{usercourse.id}{count}'
        print(certificate_id)
        return render(request,'course/completed.html',{'course':course,'user':user,'certificate_id':certificate_id})
    else:
        usercourse.save()

        return redirect(f'/course/{course.slug}/{part_no+1}')

import random
def explore(request):
    p_length = Post.objects.all().count()
    ran = [random.randrange(1,p_length,1) for i in range(int(p_length))]
    postlist = Post.objects.filter(pk__in = ran)
    return render(request,'explore.html',{'postlist':postlist})
