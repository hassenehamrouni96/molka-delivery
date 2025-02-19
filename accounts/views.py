from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import the custom form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use the custom form
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()  # Display an empty form if the request is GET

    return render(request, 'accounts/register.html', {'form': form})  # Render the form in the template

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Use Django's AuthenticationForm
        if form.is_valid():
            user = form.get_user()  # Get the authenticated user
            login(request, user)  # Log the user in

            # Debugging: Print the user role to check
            print(f"Authenticated User Role: {user.role}")

            # Check the user's role and redirect accordingly
            if user.role == 'livreur':
                return redirect('livreur_home')  # Redirect to the livreur home page
            elif user.role == 'admin':
                return redirect('admin_home')  # Redirect to the admin home page
            else:
                return redirect('home')  # Redirect to the client home page (same as home page)
    else:
        form = AuthenticationForm()  # Display empty login form if GET request

    return render(request, 'accounts/login.html', {'form': form})  # Render login form
