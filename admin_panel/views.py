from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth .decorators import login_required
from .models import Category,News

def sign_in(request):
    txt = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == '' or password == '':
           txt['error'] = "Barol yoki logenni kiriting"
           return render(request,'admin_panel/sign_in.html',txt)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('admin_cabinet')
        else:
            txt['error'] = 'Login yoki parol xato'
    return render(request,'admin_panel/sign_in.html',txt)

def sign_up(request):
    txt = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        password = request.POST.get('password')
        password_1 = request.POST.get('password_1')
        if   username == '' or email =='' or f_name=='' or l_name=='' or password == '' or password_1 == '':
            txt['error'] = 'Bosh joy mavjud'
            return render(request,'admin_panel/sign_up.html',txt)
        if password != password_1:
            txt['error'] = 'Parolni qaytib tekshiring'
            return render(request,'admin_panel/sign_up.html',txt)
        user_check = User.objects.filter(username=username)
        if len(user_check) != 0:
            txt['error'] = 'Bu foydalanuvcgi mavjud'
            return render(request,'admin_panel/sign_up.html',txt)
        user=User.objects.create_user(username=username,email=email,first_name=f_name,last_name=l_name,password=password)
        user.save()
        if user is not None:
            return redirect('sign_in')
    return render(request,'admin_panel/sign_up.html',txt)

@login_required
def logout_admin(request):
    logout(request)
    return redirect('sign_in')

@login_required
def admin_cabinet(request):
    news = News.objects.all()
    new = request.POST.get('search')
    if new != '' and new is not None:
        news = News.objects.filter(title__contains=new)
    if new == 'All':
        news = News.objects.all()
    txt = {}
    txt['news'] = news
    txt['new'] = new
    return render(request,'admin_panel/admin_cabinet.html',txt)

@login_required
def news_detel(request,news_id):
    news = News.objects.get(id=news_id)
    is_author = False
    if news.author.id == request.user.id:
        is_author = True
    return render(request,'admin_panel/news_detel.html',{'news':news,'is_author':is_author})

@login_required
def add_news(request):
    context = {}
    context['categor'] = Category.objects.all()
    if request.method== 'POST':
        title = request.POST.get('title')
        img = request.FILES.get('img')
        content = request.POST.get('content')
        ctg = request.POST.get('categor')
        categor = Category.objects.get(id=ctg)
        if title == '' or img == '' or content == '' or ctg == '' or categor == '':
            context['error'] = "Bo'sh joy mavjud"
            return render(request,'admin_panel/add_content.html',context)
        con = News(title=title,img=img,content=content,cate=categor,author=request.user)
        con.save()
    return render(request,'admin_panel/add_news.html',context)

@login_required
def delete_news(request,delete_news_id):
    news = News.objects.get(id=delete_news_id)
    if news.author.id == request.user.id:
        news.delete()
    return redirect('admin_cabinet')

@login_required
def edite_news(request,edite_news_id):
    conten = News.objects.filter(id=edite_news_id)[0]
    cate = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')   
        category = request.POST.get('categor')
        ctg = Category.objects.get(id=category)
        conten.title=title
        conten.content=content
        conten.cate=ctg
        conten.save()
        return redirect('admin_cabinet')
    return render(request,'admin_panel/add_news.html',{'con':conten,'cate':cate})
