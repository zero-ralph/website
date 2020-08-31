from ..base_imports import *


class LearningForm(forms.ModelForm):

    class Meta:
        model = Learning
        fields = ['title', 'description']

    
    def save(self, commit=True, **kwargs):
        instance = super(LearningForm, self).save(commit=False)
        if commit:
            instance.author = kwargs['author']
            instance.save()
        return instance