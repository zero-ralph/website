from .base_imports import *


urlpatterns = [
    path('', Homepage.as_view(), name='homepage')
]
