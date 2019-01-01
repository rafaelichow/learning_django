from django.shortcuts import render


posts = [
    {
        'author': 'Rafael Chow',
        'title': 'Blog Post 1',
        'content': 'First Post',
        'date_posted': 'Today'
    },
    {
        'author': 'Rafael Chow',
        'title': 'Blog Post 2',
        'content': 'Second Post',
        'date_posted': 'Someday'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about title'})

