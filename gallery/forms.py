from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=75, required=True)
    last_name = forms.CharField(max_length=75, required=True)
    email = form.EmailField(max_length=75)

    class Meta:
        model: User
        fields = ('first_name', 'last_name', 'username', 'password')