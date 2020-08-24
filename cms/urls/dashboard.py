from .base_imports import *


urlpatterns = [
    path('console/dashboard', Dashboard.as_view(), name='dashboard'),
    path('console/cms/social_media', SocialMediaView.as_view(), name='social_media'),
    path('console/cms/tags', HeroTagList.as_view(), name='tags_list' ),
    path('console/cms/tags/create', HeroTagCreate.as_view(), name='tags_create'),
    path('console/cms/tags/update/<uuid:tag_id>', HeroTagUpdate.as_view(), name='tag_update'),
    path('console/cms/tags/delete/<uuid:tag_id>', HeroTagDelete.as_view(), name='tag_delete'),
]
