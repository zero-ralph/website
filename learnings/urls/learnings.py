from .base_imports import *


urlpatterns = [
    path('learnings', LearningsList.as_view(), name='learnings'),
]