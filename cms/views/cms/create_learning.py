from ..base_imports import *


class CreateLearning(LoginRequiredMixin):
    template_name = 'cms/create_learning.html'

    def get(self, request, *args, **kwargs):
        form = LearningForm()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    
    def post(self, request, *args, **kwargs):
        form = LearningForm(request.POST)
        if form.is_valid():
            form.save(
                author=self.request.user
            )
            messages.success(self.request, 'Successfully Created Learnings')
        else:
            messages.warning(self.request, 'Something went wrong')
        return redirect(reverse('learnings_list'))