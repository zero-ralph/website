from .base_imports import *


urlpatterns = [
    path('console/register', RegisterForm.as_view(), name='register'),
    path('console/forgot-password', ForgotPassword.as_view(), name='forgot_password'),
    path('console/activate/<uuid:profile_id>', Activate.as_view(), name='activate'),
]
