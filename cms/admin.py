from django.contrib import admin
from .models import (
    About,
    Tag,
    Skill,
    SocialMedia
)

# Register your models here.
admin.site.register(About)
admin.site.register(Tag)
admin.site.register(Skill)
admin.site.register(SocialMedia)