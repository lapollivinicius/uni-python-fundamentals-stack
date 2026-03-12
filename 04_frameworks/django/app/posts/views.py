from django.shortcuts import render

# Create your views here.
def Posts(request):
    posts = [
        {
            'title': 'my first post',
            'description': 'this is my fav card',
            'created_at': '2000-10-03'
        },
        {
            'title': 'my second post',
            'description': 'this is my other fav card',
            'created_at': '2000-10-03'
        }
    ]

    return render('request', 'posts.html', {'posts': posts})

def addPost(request):
    return render('request', 'add_posts.html')