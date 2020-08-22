from .base_imports import *


urlpatterns = [
    path('console/register', RegisterForm.as_view(), name='register')
]
