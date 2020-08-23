from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import (
    ModelForm, 
    EmailField,
    
)
from django.core.exceptions import (
    ValidationError, 
    ObjectDoesNotExist
)
from django.shortcuts import get_object_or_404

from ..models import UserProfile