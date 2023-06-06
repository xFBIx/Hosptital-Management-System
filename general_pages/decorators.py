from django.shortcuts import redirect
from django.contrib.auth.models import Group

def unauthenticated_user(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return view_func(request, *args, **kwargs)
    return wrapped_func

def is_profile(view_func):
    def wrapped_func(request, *args, **kwargs):
        try :
            if Group.objects.filter(user = request.user):
                return view_func(request, *args, **kwargs)
            return redirect('make-profile')
        except:
            return view_func(request, *args, **kwargs)
    return wrapped_func

def profile(view_func):
    def wrapped_func(request, *args, **kwargs):
        if Group.objects.filter(user = request.user):
            return redirect('homepage')
        return view_func(request, *args, **kwargs)
    return wrapped_func

def allowed_users(allowed_roles=''):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):
            if allowed_roles == 'notstaff' and (not request.user.groups.all() or request.user.groups.all()[0].name == 'Patient'):
                return view_func(request, *args, **kwargs)
            elif request.user.groups.all()[0].name == allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('homepage')
        return wrapped_func
    return decorator
