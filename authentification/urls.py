# import views
from .views import RegistrationView, usernameValidationView
from django.urls import path

#????? why ? why is not working ?? to see closely ?? fix this later
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('register', RegistrationView.as_view(), name="register"),
    path('login', RegistrationView.as_view(), name="login"),
    path('validate-username', csrf_exempt(usernameValidationView.as_view()), name="validate-username")
]
