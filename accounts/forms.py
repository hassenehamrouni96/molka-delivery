from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser  # Import the CustomUser model

class CustomUserCreationForm(UserCreationForm):
    # Extra fields
    first_name = forms.CharField(max_length=30, required=True, label="Prénom")
    last_name = forms.CharField(max_length=30, required=True, label="Nom")
    email = forms.EmailField(required=True, label="Email")

    # Role dropdown
    role = forms.ChoiceField(
        choices=[('livreur', 'Livreur'), ('client', 'Client')],
        label="Rôle",
        widget=forms.Select()
    )

    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Optional: Add custom styling for form fields (e.g., Bootstrap)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
