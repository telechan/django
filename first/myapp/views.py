from django.shortcuts import render

def index(request):
    """/トップページ"""
    context = {
        'name':'telechan',
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """/aboutアバウトページ"""
    return render(request, 'myapp/about.html')

def info(request):
    """/infoインフォページ"""
    return render(request, 'myapp/info.html')