from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import the custom form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Debugging Output
            print(f"Authenticated User: {user.username}, Role: {user.role}")

            # Redirect based on user role
            if user.role == 'livreur':
                return redirect('livreur_home')  # Ensure this URL is correctly defined in urls.py
            elif user.role == 'admin':
                return redirect('admin_home')  # Ensure this URL exists
            else:
                return redirect('home')  # Default redirect for clients

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def livreur_home(request):
    return render(request, 'accounts/livreur_home.html')

def deliveries(request):
    # Logic to fetch and display deliveries for the user
    return render(request, 'accounts/deliveries.html')