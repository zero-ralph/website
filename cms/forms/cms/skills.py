from ..base_imports import *


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['name', 'percentage']


    def save(self, commit=True):
        instance = super(SkillForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance