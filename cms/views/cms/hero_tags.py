from ..base_imports import *


class HeroTagList(LoginRequiredMixin):
    template_name = 'cms/hero_tags.html'

    def get(self, request, *args, **kwargs):
        tags = Tag.objects.filter(is_deleted=False)
        form = HeroTagForm()
        context = {
            'tags': tags,
            'form': form
        }
        return render(self.request, self.template_name, context)