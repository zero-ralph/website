from ..base_imports import *


class ServiceCreate(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Succesfuly added a service')
            return redirect(reverse('services_list'))

        context = {'form': form }
        messages.warning(self.request, 'Service Create Error')
        return redirect(reverse('services_list'))