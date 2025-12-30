from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

    user_data ={

        "title": "Django developer",
        "code": "DJ001",
        "content": "Welcome to the Django blog application.",   
        "created_at": "2024-06-15 10:00:00",
    }        


    return render(request, 'blog/home.html', user_data)


def posts(request):
    posts_list = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts': posts_list})
    

    # posts_list = [
    #     {
    #         "title": "First Post",
    #         "code": "POST001",
    #         "content": "This is the content of the first post.",
    #         "created_at": "2024-06-10 09:00:00",
    #     },
    #     {
    #         "title": "Second Post",
    #         "code": "POST002",
    #         "content": "This is the content of the second post.",
    #         "created_at": "2024-06-12 14:30:00",
    #     },
    #     {
    #     "title": "Introduction to Django",
    #     "code": "POST001",
    #     "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.",
    #     "created_at": "2024-06-10 10:00:00",
    # },
    # {
    #     "title": "Mastering CSS Grid",
    #     "code": "POST002",
    #     "content": "CSS Grid Layout is a two-dimensional layout system for the web. It lets you lay out items in rows and columns.",
    #     "created_at": "2024-06-12 14:30:00",
    # },
    # {
    #     "title": "JavaScript ES6 Features",
    #     "code": "POST003",
    #     "content": "ES6 brought major changes to JavaScript, including arrow functions, classes, and template literals.",
    #     "created_at": "2024-06-15 09:15:00",
    # },
    # {
    #     "title": "Understanding APIs",
    #     "code": "POST004",
    #     "content": "API stands for Application Programming Interface. It allows different software applications to communicate with each other.",
    #     "created_at": "2024-06-18 16:45:00",
    # },
    # {
    #     "title": "Future of AI in Web Dev",
    #     "code": "POST005",
    #     "content": "Artificial Intelligence is transforming web development by automating coding tasks and personalizing user experiences.",
    #     "created_at": "2024-06-20 11:20:00",
    # }
    # ]


