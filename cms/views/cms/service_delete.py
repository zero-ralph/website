from ..base_imports import *


class ServiceDelete(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        service = get_object_or_404(Service, id=self.kwargs['service_id'])
        service.is_deleted = True
        service.save()

        messages.success(self.request, 'Successfully Deleted a Service')
        return redirect(reverse('services_list'))