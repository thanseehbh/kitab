from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from myapp.models import *
from myapp.forms import *
# Create your views here.



# Create your views here.
@login_required(login_url='myapp:login')
def home_page(request):
    return render(request,'myapp/home_page.html')

def logout_link(request):
    logout(request)
    return redirect('myapp:login')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password = password )
        if user is not None:
            login(request,user)
            return redirect('myapp:home')

    return render(request,'myapp/login_page.html')


def signup_page(request):
    register_status = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_det_form = UserDetForm(request.POST,request.FILES)

        if user_form.is_valid() and user_det_form.is_valid():
            #save UserForm
                user_s = user_form.save()
                user_s.set_password(user_s.password)
                user_s.save()
                #save UserDetForm
                user_det_s = user_det_form.save(commit = False)
                user_det_s.user = user_s
                user_det_s.save()
                register_status = True
        else:
                print(user_form.errors,user_det_form.errors)
    else:
        user_form = UserForm()
        user_det_form = UserDetForm()

    page_cntent = {"user_form":user_form,"user_details_form":user_det_form,'register_status':register_status,}
    return render(request,'myapp/signup_page.html',context=page_cntent)



    ##############################################################################


@login_required(login_url='myapp:login')
def register_page(request):
    user_s = request.user
    check_userprof = UserProfile.objects.filter(user=user_s).exists()
    check_useredu = UserEduDetails.objects.filter(user=user_s).exists()
    check_userskill = UserSkillDetails.objects.filter(user=user_s).exists()
    if check_userprof == False or check_useredu == False  or check_userskill == False:

        already_status = False
    else:
        already_status = True
    register_status = False
    if request.method == 'POST':
        # user_form = UserForm(request.POST)
        # user_det_form = UserDetForm(request.POST,request.FILES)
        user_prof_form = UserProfileForm(request.POST,request.FILES)
        user_edu_form = UserEduDetailsForm(request.POST,request.FILES)
        user_skill_form = UserSkillDetailsForm(request.POST,request.FILES)
        user_n = request.POST.get('username')
        user_s = User.objects.get(username=user_n)
        if user_prof_form.is_valid() and user_edu_form.is_valid() and user_skill_form.is_valid():

            user_prof_s = user_prof_form.save(commit = False)
            user_prof_s.user = user_s
            user_prof_s.save()
            user_edu_s = user_edu_form.save(commit = False)
            user_edu_s.user = user_s
            user_edu_s.save()
            user_skill_s = user_skill_form.save(commit = False)
            user_skill_s.user = user_s
            user_skill_s.save()
            register_status = True
        else:
                print(user_prof_form.errors,user_edu_form.errors,user_skill_form.errors)#user_form.errors,user_det_form.errors

    else:
        # user_form = UserForm()
        # user_det_form = UserDetForm()
        user_prof_form = UserProfileForm()
        user_edu_form = UserEduDetailsForm()
        user_skill_form = UserSkillDetailsForm()
    page_cntent = {'user_profile_form': user_prof_form,'user_edu_form': user_edu_form,'user_skill_form': user_skill_form,'register_status':register_status,'already_status': already_status}
    return render(request,'myapp/register_page.html',context=page_cntent)


@login_required(login_url='myapp:login')
def profile_page(request):
    user_s = request.user
    check_userprof = UserProfile.objects.filter(user=user_s).exists()
    check_useredu = UserEduDetails.objects.filter(user=user_s).exists()
    check_userskill = UserSkillDetails.objects.filter(user=user_s).exists()
    if check_userprof == False or check_useredu == False  or check_userskill == False:

        already_status = False
        page_cntent = {'no_data':'no_data'}
        pass
    else:
        already_status = True
        user_name = request.user.username
        user = User.objects.get(username=user_name)
        user_det = UserDet.objects.get(user=user)
        user_profile = UserProfile.objects.get(user=user)
        user_edu = UserEduDetails.objects.get(user=user)
        user_skill = UserSkillDetails.objects.get(user=user)
        page_cntent = {'user':user, 'user_det': user_det,'user_profile':user_profile,'user_edu':user_edu,'user_skill':user_skill,'already_status':already_status}
    return render(request,'myapp/profile_page.html',context=page_cntent)
