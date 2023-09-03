from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

from .models import User, Profile
from .forms import RegisterUser
from .utils import passwordResetEmail


########################## Authentication Section ##########################


def loginUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        user = auth.authenticate(request, phone=phone, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'خوش آمدید')
            return redirect('HOME')
        else:
            messages.error(request, 'مشخصات وارد شده اشتباه می باشد، دوباره تلاش کنید')
            return render(request, 'login.html')
    return render(request, "user/login.html")


def logoutUser(request):
    auth.logout(request)
    messages.info(request, 'به امید دیداری دوباره')
    return redirect('HOME')


########################## Register User Section ##########################


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(email=email, password=password,first_name=first_name,
                                            last_name=last_name, phone=phone)
            user.save()
            messages.success(request, 'اطلاعات شما با موفقیت ثبت گردید')
            return redirect('HOME')
        else:
            messages.error(request, f'{form.errors}')
            return redirect('REGISTER')
    else:
        form = RegisterUser()
    return render(request, "user/signup.html", {'form': form})


########################## Profile Page Section ##########################


def userProfile(request):
    if request.user.is_authenticated:
        prof = Profile.objects.get(user=request.user)
        context = {'profile':prof,}
        return render(request, 'user/profile.html', context=context)
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')


########################## Password Reset Section ##########################


def forgetPassword(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            passwordResetEmail(request, user)
            messages.success(request, 'لینک بازیابی گذر واژه با موفقیت فرستاده شد')
            return redirect('LOGIN')
        else:
            messages.error(request, 'پست الکترونیکی داده شده اشتباه می باشد')
            return redirect('FORGET')
    return render(request, 'user/forget_password.html')


def resetLink(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except:
        pass
    
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'گذر واژه خود را بازیابی کنید')
        return redirect('CONFIRM')
    else:
        messages.error(request, 'توکن نا معتبر است، یا پیش از این استفاده شده')
        return redirect('LOGIN')


def confirmResetting(request):
    if request.user.is_authenticated:
        messages.warning(request, 'شما نمیتوانید به این صفحه مراجعه کنید')
        return redirect('HOME')
    elif request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'گذر واژه با موفقیت بازیابی شد')
            return redirect('LOGIN')
        else:
            messages.error(request, 'گذر واژه های داده شده همخوانی ندارند، دوباره تلاش کنید')
            return redirect('CONFIRM')
    return render(request, 'user/confirm_password.html')
