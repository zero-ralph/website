from ..base_imports import *


class SocialMediaForm(forms.ModelForm):

    class Meta:
        model = SocialMedia
        fields = ['facebook', 'linkedin', 'instagram']


    def __init__(self, *args, **kwargs):
        super(SocialMediaForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(SocialMediaForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance