from django.urls import path
from users.views import (
    logout_view,
    LoginView,
    SignUpView,
    UserProfileView,
    UpdateProfileView,
    UpdatePasswordView,
)

app_name = "people"

urlpatterns = [
    path("logout/", logout_view, name="logout"),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/", UserProfileView.as_view(), name="profile"),
    path("update-profile/", UpdateProfileView.as_view(), name="update"),
    path("update-passwod/", UpdatePasswordView.as_view(), name="password"),
]
