from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect,render
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from .forms import *
from .models import *
from .decorators import *
from django.db.models import Q


def login_home(request):
    if request.method == 'POST':
        user_name=request.POST['username']
        pasword=request.POST['password']
        user = authenticate(request,username=user_name,password=pasword)
        if user is not None:
            login(request,user)
            return redirect('selectsplit')
        else:
            return redirect('register')
    else:
        return render(request,'exercisestracker/login_home.html')



def register_user(request):
    if request.method == 'POST':
        forms = user_register_form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('userinfo')
        else:
            return HttpResponse('error:',forms.errors )
    else:
        forms=user_register_form()
    context={'forms':forms}
    return render(request,'exercisestracker/register_user.html',context)


@loggedin_user
def user_info(request):
    if request.method == 'POST':
        forms = user_information_form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('selectsplit')
        else:
            return HttpResponse('error:',forms.errors )
    else:
        forms=user_information_form()
    context={'forms':forms}
    return render(request,'exercisestracker/user_info.html',context)


@loggedin_user
def select_split(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            return redirect('logout')
        if 'view' in request.POST:
            return redirect('userhistory')
        else:
            split_of_user = request.POST['split']
            if split_of_user == 'chest':
               return redirect('chestexercises')
            if split_of_user == 'back':
               return redirect('backexercises')
            # if split_of_user == 'legs':
            #    return redirect('legexercises')
            # if split_of_user == 'core':
            #    return redirect('coreexercises')
    else:
        return render(request,'exercisestracker/selectsplit.html')


@loggedin_user
def chestexercises(request):
    if request.method == 'POST':

        if 'back' in request.POST:
            return redirect('selectsplit')
        if 'view' in request.POST:
            return redirect('userhistory')
        if 'save' in request.POST:
            exercises = request.POST['exercises']
            set1 = request.POST['set1']
            set2 = request.POST['set2']
            set3 = request.POST['set3']
            user = request.user
            split_instance = split.objects.create(user=user,split_name='chest')
            chestexercises_instance = Chest_exercises.objects.create(split=split_instance,
                                                                     exercises=exercises,
                                                                    set1=set1,
                                                                    set2=set2,
                                                                    set3=set3,
                                                                    )
            return redirect('selectsplit')
    else:
        return render(request,'exercisestracker/chestexercises.html')

@loggedin_user
def backexercises(request):
    if request.method == 'POST':
        if 'back' in request.POST:
            return redirect('selectsplit')
        if 'view' in request.POST:
            return redirect('userhistory')
        if 'save' in request.POST:
            exercises = request.POST['exercises']
            set1 = request.POST['set1']
            set2 = request.POST['set2']
            set3 = request.POST['set3']
            user = request.user
            split_instance = split.objects.create(user=user,split_name='back')
            chestexercises_instance = Back_exercises.objects.create(split=split_instance,
                                                                    exercises=exercises,
                                                                    set1=set1,
                                                                    set2=set2,
                                                                    set3=set3,
                                                                    )
            return redirect('userhistory')
    else:
        return render(request,'exercisestracker/backexercises.html')
# @loggedin_user        
# def legexercises(request):
#     if request.method == 'POST':
#         if 'back' in request.POST:
#             return redirect('selectsplit')
#         if 'view' in request.POST:
#             return redirect('userhistory')
#         if 'save' in request.POST:
#             exercises = request.POST['exercises']
#             set1 = request.POST['set1']
#             set2 = request.POST['set2']
#             set3 = request.POST['set3']
#             user = request.user
#             split_instance = split.objects.create(user=user,split_name='leg')
#             chestexercises_instance = Back_exercises.objects.create(split=split_instance,
#                                                                     exercises=exercises,
#                                                                     set1=set1,
#                                                                     set2=set2,
#                                                                     set3=set3,
#                                                                     )
#             return redirect('userhistory')
#     else:
#         return render(request,'todolist/backexercises.html')
# @loggedin_user    
# def coreexercises(request):
#     if request.method == 'POST':
#         if 'back' in request.POST:
#             return redirect('selectsplit')
#         if 'view' in request.POST:
#             return redirect('userhistory')
#         if 'save' in request.POST:
#             exercises = request.POST['exercises']
#             set1 = request.POST['set1']
#             set2 = request.POST['set2']
#             set3 = request.POST['set3']
#             user = request.user
#             split_instance = split.objects.create(user=user,split_name='core')
#             chestexercises_instance = Back_exercises.objects.create(split=split_instance,
#                                                                     exercises=exercises,
#                                                                     set1=set1,
#                                                                     set2=set2,
#                                                                     set3=set3,
#                                                                     )
#             return redirect('userhistory')
#     else:
#         return render(request,'todolist/backexercises.html')

@loggedin_user
def user_history(request):
    if request.method == 'POST':
        if 'logout' in request.POST:
            return redirect('logout')
        if 'back' in request.POST:
            return redirect('selectsplit')
        if 'backprogress' in request.POST:
            return redirect('userhistory')
        if 'show' in request.POST:
            user = request.user
            xi={}
            context={}
            option = request.POST['body_part']
            count=0
            if option == 'chest':
                split_quary_set = split.objects.filter(Q(user=user)&Q(split_name='chest'))
                for split_instance in split_quary_set:
                    chest_quary_set = Chest_exercises.objects.filter(split=split_instance)
                    for chest_instance in chest_quary_set:
                        exercises = chest_instance.exercises
                        print(chest_instance.set1)
                        set1 = chest_instance.set1
                        set2 = chest_instance.set2
                        set3 = chest_instance.set3
                        xi={'exercises':exercises,'set1':set1,'set2':set2,'set3':set3}
                        count+=1
                        context[count]=xi
            if option == 'back':
                split_quary_set = split.objects.filter(Q(user=user)&Q(split_name='back'))
                for split_instance in split_quary_set:
                    chest_quary_set = Chest_exercises.objects.filter(split=split_instance)
                    for chest_instance in chest_quary_set:
                        exercises = chest_instance.exercises
                        print(chest_instance.set1)
                        set1 = chest_instance.set1
                        set2 = chest_instance.set2
                        set3 = chest_instance.set3
                        xi={'exercises':exercises,'set1':set1,'set2':set2,'set3':set3}
                        count+=1
                        context[count]=xi
            if option == 'legs':
                split_quary_set = split.objects.filter(Q(user=user)&Q(split_name='legs'))
                for split_instance in split_quary_set:
                    chest_quary_set = Chest_exercises.objects.filter(split=split_instance)
                    for chest_instance in chest_quary_set:
                        exercises = chest_instance.exercises
                        print(chest_instance.set1)
                        set1 = chest_instance.set1
                        set2 = chest_instance.set2
                        set3 = chest_instance.set3
                        xi={'exercises':exercises,'set1':set1,'set2':set2,'set3':set3}
                        count+=1
                        context[count]=xi
            if option == 'core':
                split_quary_set = split.objects.filter(Q(user=user)&Q(split_name='core'))
                for split_instance in split_quary_set:
                    chest_quary_set = Chest_exercises.objects.filter(split=split_instance)
                    for chest_instance in chest_quary_set:
                        exercises = chest_instance.exercises
                        print(chest_instance.set1)
                        set1 = chest_instance.set1
                        set2 = chest_instance.set2
                        set3 = chest_instance.set3
                        xi={'exercises':exercises,'set1':set1,'set2':set2,'set3':set3}
                        count+=1
                        context[count]=xi

                    
        return render(request,'exercisestracker/user_Psplit.html',{'context':context})
    else:
        return render(request,'exercisestracker/user_Hdropdown.html')

def logout_user(request):
    logout(request)
    return redirect('home')






    
