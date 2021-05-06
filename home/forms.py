from django import forms

from .models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'email',
            'password',
            'mobile'
        ]
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email should end with @gmail.com")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password)<8:
            raise forms.ValidationError("Password cannot be less than 8 characters")
        return password

    def clean_mobile(self):
        mobile = self.cleaned_data.get['mobile']
        if not mobile.isnumeric():
            raise forms.ValidationError("Mobile number should be a number")
        if len(mobile)<10:
            raise forms.ValidationError("Mobile cannot be less than 10-digits")
        return mobile