from django.urls import path
from .views import register, login, follow_user, unfollow_user

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('follow/<int:user_id>/', follow_user),
    path('unfollow/<int:user_id>/', unfollow_user),
]
from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('profile', ProfileView.as_view()),
]


