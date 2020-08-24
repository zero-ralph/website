from ..base_imports import *


class HeroTagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['name']


    def save(self, commit=True):
        instance = super(HeroTagForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance