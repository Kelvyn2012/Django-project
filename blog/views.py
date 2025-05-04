from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'kelvin',
        'title': 'blog post 1',
        'date_posted': 'August 27,2017',
         'content': 'first post content'
    },
     {
        'author': 'jude',
        'title': 'blog post 2',
        'date_posted': 'August 29,2017',
        'content': 'second post content'
    }
]


def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})