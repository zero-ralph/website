from ..base_imports import *


class SkillsView(LoginRequiredMixin):
    template_name = 'cms/skills.html'

    def get(self, request, *args, **kwargs):
        skills = Skill.objects.filter(is_deleted=False)
        form = SkillForm()
        context = {
            'skills': skills,
            'form': form
        }
        return render(self.request, self.template_name, context)