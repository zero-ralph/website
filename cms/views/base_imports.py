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
    ServiceForm,
    LearningForm
)

# common
from common.views import *

# learnings
from learnings.models import *
