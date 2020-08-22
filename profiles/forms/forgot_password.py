from .base_imports import *


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email Address', required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            user = get_object_or_404(UserProfile, email=email)
        except:
            raise ValidationError('There is no record of this email')

        return email
    
    def send_email(self):
        print('test')