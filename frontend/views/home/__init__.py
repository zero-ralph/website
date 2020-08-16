from ..base_imports import *


class Homepage(TemplateView):
    template_name = 'frontend/homepage.html'

    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name)