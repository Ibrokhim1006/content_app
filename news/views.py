from django.shortcuts import render
from admin_panel.models import Category,News

def home(request):
    txt = {}
    txt['categor'] = Category.objects.all()
    txt['news'] = News.objects.all()
    return render(request,'news/index.html',txt)

def categor(request,cate_id):
    txt = {}
    txt['categor'] = Category.objects.all()
    txt['cate'] = Category.objects.get(id=cate_id)
    txt['content'] = News.objects.filter(cate=cate_id)
    return render(request,'news/index.html',txt)

def detel_news(request,new_id):
    txt = {}
    txt['categor'] = Category.objects.all()
    txt['detel'] = News.objects.filter(id=new_id)
    return render(request,'news/index.html',txt)

