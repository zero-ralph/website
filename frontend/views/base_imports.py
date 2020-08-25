from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
)
from django.template.loader import render_to_string
from django.views.generic import (
    TemplateView, 
    CreateView,
    UpdateView,
    FormView
)

# cms
from cms.models import (
    SocialMedia, 
    Tag,
    About
)

# common app
from common.tasks import *

# profiles app 
from profiles.forms import (
    RegistrationForm,
    ForgotPasswordForm,
)
from profiles.models import UserProfile