from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic

from .forms import StyledAuthenticationForm, StyledUserCreationForm

class SignUpView(generic.CreateView):
    form_class = StyledUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = StyledAuthenticationForm
