# import views
from .views import RegistrationView
from django.urls import path

urlpatterns = [

    path('register', RegistrationView.as_view(), name="register"),
    path('login', RegistrationView.as_view(), name="login")
]
