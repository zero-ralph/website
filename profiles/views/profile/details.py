from ..base_imports import *


class Profile(LoginRequiredMixin):
    template_name = 'profile/details.html'

    def get(self, request, *args, **kwargs):
        current_user = request.user
        form = ProfileForm(instance=current_user.profile)
        context = {
            'current_user': current_user,
            'form': form
        }
        return render(self.request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        instance = get_object_or_404(UserProfile, id=self.kwargs['profile_uuid'])
        form = ProfileForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Updated Profile')
            return redirect(
                reverse('profile_details', kwargs={'profile_uuid': instance.id})
            )
        
        messages.warning(self.request, 'Form Error')
        return render(self.request, self.template_name, context)