from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import login as authlogin

from django.contrib.auth.forms import UserCreationForm
from .models import *
from contents.models import *
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password = raw_password)
            authlogin(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        if username and raw_password:
            print(raw_password,username)
            user = authenticate(username=username,password = raw_password)
            authlogin(request,user)
            return redirect('/')
    
    return render(request,'login.html',)

def loggingout(request):
    logout(request)
    messages.info(request,"You have successfully logged out.")
    return redirect('/')


def dashboard(request):
    user = request.user
    profile = User.objects.get(id=user.id)
    courses = UserCourse.objects.filter(user=user,completed=False)
    completed_course = UserCourse.objects.filter(user=user,completed=True)
    skillsets,skillsetscreate = SkillSets.objects.get_or_create(user=user)

    progresses =[]
    # course_list =[]
    # for i in courses:
    #     course_list.append(i)
    
    # for i in courses:
    #     l = CourseOrdering.objects.filter(course=i.course)
    #     for j in l:

    

    return render(request,'dashboard.html',{'courses':courses,'progresses':progresses,'profile':profile,'completed_course':completed_course,'skillsets':skillsets})
    
    

def profile(request):
    user = request.user
    profession_list = Ikigais.objects.all()
    profile = User.objects.get(username=user)
    ikigais,ikigais2 =UserIkigai.objects.get_or_create(user=user)
    professions={}
    hobbies={}
    interests={}


    if ikigais:
        for i in range(5):
            if (i !=0) and (i < 6):
                name=f'professsion_ikigai{i}'
                values =f'profession_ikigai{i}_value'
                values =getattr(ikigais,values)
                p = getattr(ikigais,name)
                if p != None:
                    professions[p]=values
             
            
                name=f'interest_ikigai{i}'
                values =f'interest_ikigai{i}_value'
                values =getattr(ikigais,values)
                p = getattr(ikigais,name)
                if p != None:
                    interests[p]=values
            
                name=f'hobby_ikigai{i}'
                values =f'hobby_ikigai{i}_value'
                values =getattr(ikigais,values)
                p = getattr(ikigais,name)
                if p != None:
                    hobbies[p]=values


    else:

        for i in range(5):
            if (i !=0) and (i < 6):
                name=f'professsion_ikigai{i}'
                values =f'profession_ikigai{i}_value'
                values =getattr(ikigais2,values)
                p = getattr(ikigais2,name)
                if p != None:
                    professions[p]=values
             
            
                name=f'interest_ikigai{i}'
                values =f'interest_ikigai{i}_value'
                values =getattr(ikigais2,values)
                p = getattr(ikigais2,name)
                if p != None:
                    interests[p]=values
            
                name=f'hobby_ikigai{i}'
                values =f'hobby_ikigai{i}_value'
                values =getattr(ikigais2,values)
                p = getattr(ikigais2,name)
                if p != None:
                    hobbies[p]=values
            
    print(professions,hobbies,interests)

    return render(request,'profile.html',{'profile':profile,'ikigais':ikigais,'professions':professions,'hobbies':hobbies,'interests':interests,'professionlist':profession_list,})

from .forms import ProfessionIkigaiForm,HobbyIkigaiForm,InterestIkigaiForm, ProfileForm
from django.contrib import messages

def updateprofessions(request):
    user = request.user
    profession_list = Ikigais.objects.all()
    userikigai = UserIkigai.objects.get(user=user)
    form = ProfessionIkigaiForm(request.POST,instance=userikigai)
    if form.is_valid():
        form.save()
        messages.success(request, 'Professions Updated! Changes successfully saved.')

    else:
        form = ProfessionIkigaiForm()
    # return render(request,'professionikigaiform.html',{'form':form,'professionlist':profession_list})

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def updateprofile(request):
    user = request.user
    profile,profile2 = Profile.objects.get_or_create(user=user)
    uservalues = user

    # form = ProfileForm(request.POST,instance=profile)

    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        age = request.POST.get('age')
        address = request.POST.get('address')
        print("ADDRESS",address)
        address = Location.objects.get(id = address)
        # profilephoto = request.FILES['profilephoto']

        u  = User.objects.get(id=user.id)
        u.first_name = first_name
        u.last_name = last_name
        u.save()
        print("first",u.username,u.first_name,u.last_name)

        if profile:
            profile.age = age
            profile.address= address
            profile.gender = request.POST.get('gender')

            profile.save()
        else:
            profile2.age = age
            profile2.address= address
            profile2.gender = request.POST.get('gender')

            profile2.save()


        return redirect('/profile')

    # if form.is_valid():
    #     form.save()
    #     messages.success(request,'Profile Updated')
    # else:
    #     form = ProfileForm()

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'updateprofile.html',{'profile':profile,'uservalues':uservalues})


def updatehobbies(request):
    user = request.user
    # profession_list = Ikigais.objects.all()
    userikigai = UserIkigai.objects.get(user=user)
    form = HobbyIkigaiForm(request.POST,instance=userikigai)
    if form.is_valid():
        form.save()
        messages.success(request, 'Hobbies Updated! Changes successfully saved.')

    else:
        form = HobbyIkigaiForm()
    # return render(request,'professionikigaiform.html',{'form':form,'professionlist':profession_list})

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def updateinterests(request):
    user = request.user
    # profession_list = Ikigais.objects.all()
    userikigai = UserIkigai.objects.get(user=user)
    form = InterestIkigaiForm(request.POST,instance=userikigai)
    if form.is_valid():
        form.save()
        messages.success(request, 'Interest Updated! Changes successfully saved.')

    else:
        form = InterestIkigaiForm()
    # return render(request,'professionikigaiform.html',{'form':form,'professionlist':profession_list})

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))