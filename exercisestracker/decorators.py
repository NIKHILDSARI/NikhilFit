from django.contrib.auth import authenticate,login
from django.shortcuts import redirect

def loggedin_user(view_func):
    def wrapper_func(request,*arg,**kwarg):
        if request.user.is_authenticated:
            return view_func(request,*arg,**kwarg)
        else:
            return redirect('home')
    return wrapper_func

