from .base_imports import *


class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'middle_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(ProfileForm, self).save(commit=False)
        if commit:
            instance.save()
        return instance