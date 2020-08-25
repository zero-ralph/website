from ..base_imports import *


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ['name', 'description', 'icon']

    
    def save(self, commit=True):
        instance = super(ServiceForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance
