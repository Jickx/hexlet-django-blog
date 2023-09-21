from django.shortcuts import render, redirect


def index(request):
    return redirect('python/42/', tags='python', articles_id='42')


def article(request, tags, article_id):
    return render(request, 'articles/index.html', context={
        'tags': tags,
        'article_id': article_id,
    })
