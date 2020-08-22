from .base_imports import *


urlpatterns = [
    path('console/register', RegisterForm.as_view(), name='register'),
    path('console/forgot-password', ForgotPassword.as_view(), name='forgot_password')
]
