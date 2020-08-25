from django.contrib import messages
from django.shortcuts import (
    render,
    reverse,
    redirect, 
    get_object_or_404
)

from ..models import (
    SocialMedia, 
    Tag,
    About
)
from ..forms import (
    SocialMediaForm, 
    HeroTagForm,
    AboutForm,
)

# common
from common.views import *
