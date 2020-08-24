from ..base_imports import *


class HeroTagCreate(LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        print('test')
        form = HeroTagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Created a Tag')
            return redirect(reverse('tags_list'))
        
        context = {'form': form}
        messages.warning(self.request, 'Create Tag Error')
        return redirect(reverse('tags_list'))