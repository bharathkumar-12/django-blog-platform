from django.urls import path

from .views import SignUpView, UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
