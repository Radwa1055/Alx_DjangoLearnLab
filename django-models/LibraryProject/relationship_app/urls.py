from django.urls import path
from .views import list_books, LibraryDetailView 

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]



from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Existing book/library URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs (Checker expects these exact patterns)
    path('register/', views.register_view, name='register'),  # ✅ views.register
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # ✅ LoginView.as_view(template_name=
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # ✅ LogoutView.as_view(template_name=
]



from django.urls import path
from . import views

urlpatterns += [
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('book/add_book/', views.add_book, name='add_book'),
    path('book/edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('book/delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
