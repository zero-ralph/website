from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.views.generic import (
    TemplateView, 
    CreateView,
    FormView
)
from profiles.forms import (
    RegistrationForm,
    ForgotPasswordForm,
)