from ..base_imports import *


class ServiceUpdate(LoginRequiredMixin):
    
    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Service, id=self.kwargs['service_id'])
        form = ServiceForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Updated a Service')
            return redirect(reverse('services_list'))

        context = {
            'form': form,
            'instance': instance
        }
        messages.warning(self.request, 'Update Service Error')
        return redirect(reverse('services_list'))