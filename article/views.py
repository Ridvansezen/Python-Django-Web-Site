from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def projects(request):
    return render(request,"projects.html")
@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarıyla Oluşturuldu...")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    return render(request,"detail.html",{"article":article})
@login_required(login_url = "user:login")
def editarticle(request,id):
    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarıyla Düzenlendi...")
        return redirect("index")

    return render(request,"editarticle.html",{"form":form})
@login_required(login_url = "user:login")
def deletearticle(request,id):
    article = get_object_or_404(Article,id = id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi...")
    return redirect("index")
