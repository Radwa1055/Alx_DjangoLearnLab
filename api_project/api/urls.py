from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]



#task 2
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
 # final task 
 
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
urlpatterns += [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
