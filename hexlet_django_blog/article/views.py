from django.shortcuts import render


def index(request):
    return render(request, 'articles/index.html', context={
        'app_name': __package__.split('.')[1]
    })
