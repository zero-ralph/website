from .base_imports import *


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    username = forms.CharField(label='Username', required=True)
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', required=True, widget=forms.PasswordInput)


    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user = User.objects.filter(email=email)
        if user.count() > 0:
            raise ValidationError('Email already exists')
        return email


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        user = User.objects.filter(username=username)
        if user.count() > 0:
            raise ValidationError('Username already exists')
        return username

    
    def clean_password(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User()
        user.username = self.cleaned_data['username']
        user.password = make_password(self.cleaned_data['password1'])
        # user.is_active = False
        user.save()

        profile = UserProfile()
        profile.user = user
        profile.email = self.cleaned_data['email']
        profile.save()

        return user
    