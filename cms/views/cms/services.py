from ..base_imports import *


class ServicesView(LoginRequiredMixin):
    template_name = 'cms/services.html'

    def get(self, request, *args, **kwargs):
        services = Service.objects.filter(is_deleted=False)
        form = ServiceForm()

        context = {
            'services': services,
            'form': form
        }
        return render(self.request, self.template_name, context)