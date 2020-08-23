from ..base_imports import *
from django.contrib.auth.decorators import login_required



class Dashboard(LoginRequiredMixin):
    template_name = 'cms/dashboard.html'

    def get(self, request, *args, **kwargs):
        absolute_path = self.request.scheme + '://' + self.request.get_host()
        print(absolute_path)
        return render(self.request, self.template_name)
