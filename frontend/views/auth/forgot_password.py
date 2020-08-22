from ..base_imports import *


class ForgotPassword(FormView):
    template_name = 'registration/forgot_password.html'

    def get(self, request, *args, **kwargs):
        form = ForgotPasswordForm()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(self.request, 'An email has been sent into your email.')
            return redirect(reverse('login'))
        
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)