from django.shortcuts import render, redirect

from firstapp.models import Article, Comment, Ticket, UserProfile
from firstapp.forms import CommentForm, EditInfoForm

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    request_type = request.GET.get('tag')
    if request.GET.get('tag'):
        article_list = Article.objects.filter(tag=request_type)
    else:
        article_list = Article.objects.all()
    page_robot = Paginator(article_list, 3)
    page_num = request.GET.get('page')
    try:
        article_list = page_robot.page(page_num)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
        
    context = {}
    context["article_list"] = article_list
    context["tag"] = request_type
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)

    if request.method == "GET":
        form = CommentForm

    context = {}
    context["article"] = article
    context['form'] = form
    
    return render(request, 'detail.html', context)

def comment(request, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            comment = form.cleaned_data["comment"]
            article = Article.objects.get(id=id)
            c = Comment(name=name, comment=comment, belong_to=article)
            c.save()
            return redirect(to="detail", id=id)
    return redirect(to="detail", id=id)


def index_login(request):
    context = {}
    if request.method == "GET":
        form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index")
    context['form'] = form
    return render(request, 'login.html', context)


def index_register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)


def vote(request, id):
    # 未登录用户不允许投票，自动跳回详情页
    if not isinstance(request.user, User):
        return redirect(to="detail", id=id)

    voter_id = request.user.id

    try:
        # 如果找不到登陆用户对此篇文章的操作，就报错
        user_ticket_for_this_article = Ticket.objects.get(voter_id=voter_id, article_id=id)
        user_ticket_for_this_article.choice = request.POST["vote"]
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, article_id=id, choice=request.POST["vote"])
        new_ticket.save()

    # 如果是点赞，更新点赞总数
    if request.POST["vote"] == "like":
        article = Article.objects.get(id=id)
        article.likes += 1
        article.save()

    return redirect(to="detail", id=id)


def editInfo(request, id):
    if request.method == "POST":
        form = EditInfoForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            sex = request.POST["sex"]
            user = User.objects.get(id=id)
            if UserProfile.objects.get(belong_to__username=user.username):
                profile = UserProfile.objects.get(belong_to__username=user.username)
                if name != '':
                    profile.nickname = name
                profile.sex = sex
                if request.FILES:
                    profile.avatar = request.FILES['avatar']
                profile.save()
            else:
                if request.FILES:
                    avatar = request.FILES['avatar']
                    profile = UserProfile(nickname=name, sex=sex, avatar=avatar, belong_to=user)
                else:
                    profile = UserProfile(nickname=name, sex=sex, belong_to=user)
                profile.save()
    return redirect(to="myInfo", id=id)


def myinfo(request, id):
    context = {}
    if request.method == "GET":
        form = EditInfoForm
    context['form'] = form
    return render(request, 'myInfo.html', context)


def mycollection(request):
    context = {}
    collections = Article.objects.filter(article_tickets__choice='like', article_tickets__voter=request.user)
    page_robot = Paginator(collections, 3)
    page_num = request.GET.get('page')
    try:
        collections = page_robot.page(page_num)
    except EmptyPage:
        collections = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        collections = page_robot.page(1)
    context['collections'] = collections
    return render(request, 'myCollection.html', context)
