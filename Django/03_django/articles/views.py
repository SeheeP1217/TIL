from django.shortcuts import render, redirect
from articles.models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    #return render(request, 'articles/create.html')
    return redirect('articles:detail', article.pk)
    # 글작성완료 화면을 띄울 필요 없이 바로 글이 작성된 화면으로 바로 갈 수 있음

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article':article}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    title = request.POST.get('title')
    content = request.POST.get('content')
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)