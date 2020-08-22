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
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(self.request, user)
            return redirect(reverse('homepage'))
        
        
        context = {'form': form }
        return render(self.request, self.template_name, context)