from ..base_imports import *


class HeroTagUpdate(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Tag, id=self.kwargs['tag_id'])
        form = HeroTagForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Succesfully updated a Tag')
            return redirect(reverse('tags_list'))
            
        context = {
            'instance': instance,
            'form': form
        }
        return redirect(reverse('tags_list'))