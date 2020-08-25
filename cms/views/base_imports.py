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
    About,
    Skill,
    Service
)
from ..forms import (
    SocialMediaForm, 
    HeroTagForm,
    AboutForm,
    SkillForm,
    ServiceForm
)

# common
from common.views import *
