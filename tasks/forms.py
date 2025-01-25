# tasks/forms.py

from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import Task  # Import the Task model

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']  # Specify the fields you want in the form

    # You can add custom validation or methods here if necessary
# tasks/forms.py

# from django import forms
# from .models import Task

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description']  # Remove 'completed' from the list if it shouldn't exist


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        
        return cleaned_data
