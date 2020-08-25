from ..base_imports import *


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = [
            'subtitle', 'position_header', 'position_sub_header', 'location'
        ]


    def __init__(self, *args, **kwargs):
        super(AboutForm, self).__init__(*args, **kwargs)


    def save(self, commit=True):
        instance = super(AboutForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance