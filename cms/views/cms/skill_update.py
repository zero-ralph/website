from ..base_imports import *


class SkillUpdate(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(Skill, id=self.kwargs['skill_id'])
        form = SkillForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Skill Successfully Updated')
            return redirect(reverse('skills_list'))

        context = {
            'form': form,
            'instance': instance
        }
        messages.warning(self.request, 'Skill Update Error')
        return redirect(reverse('skills_lsit'))