from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class StyledAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'})
    )


class StyledUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w-full rounded-lg border border-slate-200 px-4 py-2'})
    )
