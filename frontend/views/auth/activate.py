from ..base_imports import *


class Activate(UpdateView):
    
    def get(self, request, *args, **kwargs):
        try:
            profile = get_object_or_404(UserProfile, id=self.kwargs['profile_id'])
            profile.user.is_active = True
            profile.user.save()
            messages.success(self.request, 'Activation Success. Please Logged In')
        except:
            raise ValidationError('User non-existent')
        return redirect(reverse('login'))