from ..base_imports import *


class HeroTagDelete(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Tag, id=self.kwargs['tag_id'])
        instance.is_deleted = True
        instance.save()

        return redirect(reverse('tags_list'))