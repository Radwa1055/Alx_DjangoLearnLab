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

from django.urls import path
from .views import (
    FollowUserView,
    UnfollowUserView
)

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view()),
]


from django.urls import path
from .views import followuser, unfollowuser

urlpatterns = [
    path('follow/<int:user_id>/', followuser),
    path('unfollow/<int:user_id>/', unfollowuser),
]

from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view()),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view()),
]

/follow/int:user_id/
/unfollow/int:user_id/
