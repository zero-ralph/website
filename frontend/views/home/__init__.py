from ..base_imports import *


class Homepage(TemplateView):
    template_name = 'frontend/homepage.html'

    def get(self, request, *args, **kwargs):
        social_media = get_object_or_404(SocialMedia, id=1)
        context = {
            'social_media': social_media
        }

        return render(self.request, self.template_name, context)