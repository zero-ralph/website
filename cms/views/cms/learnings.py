from ..base_imports import *


class LearningList(LoginRequiredMixin):
    template_name = 'cms/learnings.html'

    def get(self, request, *args, **kwargs):
        learnings = Learning.objects.filter(is_deleted=False)
        context = {
            'learnings': learnings
        }
        return render(self.request, self.template_name, context)