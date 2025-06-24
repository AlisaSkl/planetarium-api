from django.urls import path
from user.views import CreateUserView, LoginUserView
from rest_framework.authtoken import views

urlpatterns = [
    path("login/", LoginUserView.as_view(), name="get_token"),
    path("register/", CreateUserView.as_view(), name="create")
]

app_name = "user"
