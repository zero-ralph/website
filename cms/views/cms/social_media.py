from ..base_imports import *


class SocialMediaView(LoginRequiredMixin):
    template_name = 'cms/social_media.html'

    def get(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(SocialMedia, id=1)
            form = SocialMediaForm(instance=instance)
        except:
            form = SocialMediaForm()
        
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    
    def post(self, request, *args, **kwargs):
        try:
            instance = get_object_or_404(SocialMedia, id=1)
            form = SocialMediaForm(request.POST, instance=instance)
        except:
            form = SocialMediaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Update Social Media')
            return redirect(reverse('social_media'))

        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)