from .base_imports import *


urlpatterns = [
    path('', include('frontend.urls')),
    # cms
    path('', include('cms.urls')),

    # profile
    path('', include('profiles.urls')),

    # users
    path('console/', include('django.contrib.auth.urls'))
]