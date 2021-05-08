from django import forms

from .models import User

class UserModelForm(forms.ModelForm):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',
                                                                             'placeholder':'Enter your first name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control',
                                                                            'placeholder':'Enter your last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder':'Enter your email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                                'placeholder':'Enter your password'}))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control',
                                                                            'placeholder':'Enter your mobile'}))

    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'email',
            'password',
            'mobile'
        ]

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if len (firstname) < 3:
            raise forms.ValidationError("First name cannot be less than 3 characters")
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if len (lastname) < 3:
            raise forms.ValidationError("Last name cannot be less than 3 characters")
        return lastname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email should end with @gmail.com")
        for instance in User.objects.all():
            if instance.email == email:
                raise forms.ValidationError('An account already exists with the given email', email)
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('length should be of at least 8 characters')
        if (not any(char.isdigit() for char in password)) or (not any(char.isupper() for char in password)) or (not any(char.islower() for char in password)):
            raise forms.ValidationError('Password should have at least one numeral,uppercase letter,lowercase letter')
        return password

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isnumeric():
            raise forms.ValidationError("Mobile number should be a number")
        if len(mobile)<10:
            raise forms.ValidationError("Mobile cannot be less than 10-digits")
        return mobile

class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Enter your password'}))
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email should end with @gmail.com")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('length should be of at least 8 characters')
        if (not any(char.isdigit() for char in password)) or (not any(char.isupper() for char in password)) or (not any(char.islower() for char in password)):
            raise forms.ValidationError('Password should have at least one numeral,uppercase letter,lowercase letter')
        return password

class UserViewForm(UserModelForm, forms.ModelForm):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'readonly':'readonly'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'readonly':'readonly'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'readonly': 'readonly'}))
    password = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                'readonly':'readonly'}))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'readonly':'readonly'}))

class UserUpdateForm(forms.ModelForm):
    firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Enter your new first name'}))
    lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Enter your new last name'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Enter your new password'}))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Enter your new mobile'}))
    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'password',
            'mobile'
        ]

    def clean_firstname(self):
        firstname = self.cleaned_data.get('firstname')
        if len (firstname) < 3:
            raise forms.ValidationError("First name cannot be less than 3 characters")
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data.get('lastname')
        if len (lastname) < 3:
            raise forms.ValidationError("Last name cannot be less than 3 characters")
        return lastname

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('length should be of at least 8 characters')
        if (not any(char.isdigit() for char in password)) or (not any(char.isupper() for char in password)) or (not any(char.islower() for char in password)):
            raise forms.ValidationError('Password should have at least one numeral,uppercase letter,lowercase letter')
        return password

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile.isnumeric():
            raise forms.ValidationError("Mobile number should be a number")
        if len(mobile)<10:
            raise forms.ValidationError("Mobile cannot be less than 10-digits")
        return mobile
