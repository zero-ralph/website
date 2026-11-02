from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import LandingPage

class IndexView(TemplateView): 

    template_name = "website/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Personal Website"
        context['landing_page'] = get_object_or_404(LandingPage, id=1)
        return context 
