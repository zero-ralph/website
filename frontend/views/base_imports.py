from django.contrib.auth import authenticate, login
from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.views.generic import (
    TemplateView, 
    CreateView,
)
from profiles.forms import RegistrationForm