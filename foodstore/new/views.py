from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Category, Dish
from .forms import PostForm, RegistrationForm, LoginForm

# Create your views here.


def index(request):
    posts = Dish.objects.all()

    context = {
        'posts': posts,
        "title": "Barcha yangiliklar!"
    }

    return render(request, 'index.html', context)


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Dish.objects.filter(category_id=category_id)
    context = {
        "posts": posts,
        "title": f"{category.name}: Barcha maqolalar!"
    }
    return render(request, "index.html", context)


def post_detail(request: WSGIRequest, pk):
    post = get_object_or_404(Dish, pk=pk)

    post.views += 1
    post.save()

    context = {
        "post": post,
        "title": post.name
    }
    return render(request, 'detail.html', context)


def add_post(request: WSGIRequest):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.create()
            return redirect('detail', pk=post.pk)
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, 'add_post.html', context)


def update_post(request: WSGIRequest, pk: int):
    post = get_object_or_404(Dish, pk=pk)

    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post.name = form.cleaned_data.get("name")
            post.description = form.cleaned_data.get("content")
            post.photo = form.cleaned_data.get("photo") if form.cleaned_data.get("photo") else post.photo
            post.category = form.cleaned_data.get("category")
            post.save()
            return redirect('detail', pk=post.pk)

    form = PostForm(initial={
        "name": post.name,
        "description": post.description,
        "photo": post.photo,
        "category": post.category,
    })

    context = {
        "form": form,
        'post': post
    }

    return render(request, 'add_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Dish, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')

    context = {
        "post": post
    }
    return render(request, 'confirm_delete.html', context)



def register(request: WSGIRequest):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            password = request.POST["password"]
            password_repeat = request.POST["password_repeat"]
            if password == password_repeat:
                username = request.POST['username']
                email = request.POST['email']
                user = User.objects.create_user(username, email, password)
                print("Siz ro'yxatdan o'tdingiz!")
                return redirect('login')

    else:
        form = RegistrationForm()

    context = {
        "form": form
    }
    return render(request, "auth/register.html", context)



def login_view(request: WSGIRequest):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Xush kelibsiz!")
                return redirect('home')
            else:
                print("Username yoki parol hato")
    else:
        form = LoginForm()
    context = {
        "form": form
    }
    return render(request, "auth/login.html", context)


def logout_view(request: WSGIRequest):
    logout(request)
    return redirect('login')