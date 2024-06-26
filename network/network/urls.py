
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:user>", views.profile_view, name="profile_view"),
    path("following", views.following_view, name="following_view"),

    # API routes
    path("follow", views.follow, name="follow"),
    path("post", views.post, name="post"),
    path("get_user", views.get_user, name="get_user"),
    path("like", views.like, name="like"),
    path("edit", views.edit, name="edit")
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)