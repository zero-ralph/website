from ..base_imports import *


class Homepage(TemplateView):
    template_name = 'frontend/homepage.html'

    def get(self, request, *args, **kwargs):
        social_media = get_object_or_404(SocialMedia, id=1)
        tags = Tag.objects.filter(is_deleted=False)
        about = get_object_or_404(About, id=1)
        context = {
            'social_media': social_media,
            'tags': tags,
            'about': about
        }

        return render(self.request, self.template_name, context)