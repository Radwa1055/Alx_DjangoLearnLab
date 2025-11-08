from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library 
from .models import Book     

# Function-based view
def list_books(request):
    books = Book.objects.all()
    if request.GET.get('format') == 'txt':
        output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(output, content_type="text/plain")
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in user immediately after registration
            return redirect('list_books')  # Redirect to a page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Login view using Django built-in LoginView
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True


# Logout view using Django built-in LogoutView
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
