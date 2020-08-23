from .base_imports import *


urlpatterns = [
    path('console/dashboard', Dashboard.as_view(), name='dashboard')
]
