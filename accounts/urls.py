
from django.urls import path, include
from .views.login_view import login
from .views.register_view import register

from .views.login_view import login
app_name ='accounts'
urlpatterns = [
  path("login/", login, name="login"),
    path('register/', register, name='register'),
#  path("accounts/", include("django.contrib.auth.urls")),
]