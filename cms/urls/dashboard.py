from .base_imports import *


urlpatterns = [
    path('console/dashboard', Dashboard.as_view(), name='dashboard'),
    path('console/cms/social_media', SocialMediaView.as_view(), name='social_media'),
    path('console/cms/tags', HeroTagList.as_view(), name='tags_list' ),
    path('console/cms/tags/create', HeroTagCreate.as_view(), name='tags_create'),
    path('console/cms/tags/update/<uuid:tag_id>', HeroTagUpdate.as_view(), name='tag_update'),
    path('console/cms/tags/delete/<uuid:tag_id>', HeroTagDelete.as_view(), name='tag_delete'),
    path('console/cms/about', AboutView.as_view(), name='about'),
    path('console/cms/skills', SkillsView.as_view(), name='skills_list'),
    path('console/cms/skills/create', SkillCreate.as_view(), name='skill_create'),
    path('console/cms/skills/update/<uuid:skill_id>', SkillUpdate.as_view(), name='skill_update'),
    path('console/cms/skills/delete/<uuid:skill_id>', SkillDelete.as_view(), name='skill_delete'),

]
