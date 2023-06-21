from django.shortcuts import render
from .models import News

menu = [
    {"title": "Вход", "url_name": "entrance"},
    {"title": "Регистрация", "url_name": "register"},
    {"title": "Добавить статью", "url_name": "addnews"},
    {"title": "Пожертвования", "url_name": "donations"},
]


def homes(request):
    new = News.objects.all()
    return render(request, "LokalNews/homes.html", {"new": new, "menu": menu})


def add_news(request):
    return render(request, "LokalNews/addnews.html", {"menu": menu})


def entrance(request):
    return render(request, "LokalNews/entrance.html", {"menu": menu})


def register(request):
    return render(request, "LokalNews/register.html", {"menu": menu})


def donations(request):
    return render(request, "LokalNews/donations.html", {"menu": menu})


def show_post(request, post_id):
    return render(request, f"Статья с id = {post_id}")
