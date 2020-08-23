from ..base_imports import *


class RegisterForm(CreateView):
    template_name = 'registration/register.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)

    
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            absolute_path = self.request.scheme + '://' + self.request.get_host()
            send_register_email(
                'Activate your account',
                render_to_string(
                    'registration/mails/register_email.html',
                    {
                        'base_url': absolute_path,
                        'profile': user.profile.id
                    }, self.request
                ),
                (form.cleaned_data['email'], )
            )
            messages.success(self.request, 'An email activation has been sent to your email.')
            return redirect(reverse('login'))
        
        
        context = {'form': form }
        return render(self.request, self.template_name, context)