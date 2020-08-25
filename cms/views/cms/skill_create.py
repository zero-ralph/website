from ..base_imports import *


class SkillCreate(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Created a Skill')
            return redirect(reverse('skills_list'))
        
        context = {'form': form}
        messages.warning(self.request, 'Create Skill Error')
        return redirect(reverse('skills_list'))