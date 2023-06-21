from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.homes, name="homes"),
    path("addnews/", views.add_news, name="addnews"),
    path("entrance/", views.entrance, name="entrance"),
    path("register/", views.register, name="register"),
    path("donations/", views.donations, name="donations"),
    path("post/<int:post_id>/", views.show_post, name="post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
