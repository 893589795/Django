from django.shortcuts import render, Http404, redirect, HttpResponse
from blog_app.models import Video
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# 首页
def index(request):
    context = {}
    video_list = Video.objects.all()
    page_robot = Paginator(video_list, 2)
    page_num = request.GET.get('page')
    try:
        video_list = page_robot.page(page_num)
    except EmptyPage:
        video_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        video_list = page_robot.page(1)
    context['video_list'] = video_list
    return render(request, 'index.html', context)


# 登录
def blog_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
        return redirect(to='index')
    context['form'] = form
    return render(request, 'login.html', context)


# 注册
def blog_register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register.html', context)
