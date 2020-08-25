from ..base_imports import *


class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ['name', 'percentage']

    