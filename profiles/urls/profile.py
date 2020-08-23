from .base_imports import *


urlpatterns = [
    path('console/profile/<uuid:profile_uuid>', Profile.as_view(), name='profile_details')
]
