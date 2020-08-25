from ..base_imports import *


class AboutView(LoginRequiredMixin):
    template_name = 'cms/about.html'

    def get(self, request, *args, **kwargs):
        context = {}
        try:
            instance = get_object_or_404(About, id=1)
            form = AboutForm(instance=instance)
            context['instance'] = instance
        except:
            form = AboutForm()
            
        context['form'] = form
        
        return render(self.request, self.template_name, context)

    
    def post(self, request, *args, **kwargs):
        context = {}
        try:
            instance = get_object_or_404(About, id=1)
            form = AboutForm(request.POST, instance=instance)
            context['instance'] = instance
        except:
            form = AboutForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Successfully Updated About')
            return redirect(reverse('about'))
        
        context['form'] = form
        messages.warning(self.request, 'Something Error Occured')
        return render(self.request, self.template_name, context) 
        