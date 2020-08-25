from ..base_imports import *


class SkillDelete(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        skill = get_object_or_404(Skill, id=self.kwargs['skill_id'])
        skill.is_deleted = True
        skill.save()

        messages.success(self.request, 'Skill successfully deleted')
        return redirect(reverse('skills_list'))