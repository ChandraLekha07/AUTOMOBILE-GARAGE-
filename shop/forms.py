from django import forms

from home.models import User
from .models import SellCar

class SellCarModelForm(forms.ModelForm):
    fullname = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                                         'placeholder':'Enter your email'}))
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class':'form-control',
                                                                      'placeholder':'Enter otp'}))
    STATE_CHOICES = [
        ('', 'SELECT STATE'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Orissa', 'Orissa'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttaranchal', 'Uttaranchal'),
        ('West Bengal', 'West Bengal'),
    ]
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    CITY_CHOICES = [
        ('', 'SELECT CITY'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Chandigarh', 'Chandigarh'),
        ('Coimbatore', 'Coimbatore'),
        ('Gurgaon', 'Gurgaon'),
        ('Hyderabad', 'Hyderabad'),
        ('Jaipur', 'Jaipur'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Noida', 'Noida'),
        ('Thane', 'Thane'),
        ('Patna', 'Patna'),
        ('Pune', 'Pune'),
    ]
    city = forms.ChoiceField(choices=CITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    MAKE_CHOICES = [
        ('', 'Select Make'),
        ('BENZ', 'Benz'),
        ('AUDI', 'Audi'),
        ('BMW', 'BMW'),
        ('TOYOTA', 'Toyota'),
        ('SUZUKI', 'Suzuki'),
    ]
    make = forms.ChoiceField(choices=MAKE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    NAME_CHOICES = [
        ('', 'Select Model'),
        ('one', 'M1'),
        ('two', 'M2'),
        ('three', 'M3'),
        ('four', 'M4'),
        ('five', 'M5'),
    ]
    name = forms.ChoiceField(choices=NAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    VARIANT_CHOICES = [
        ('', 'Select Variant'),
        ('sedan', 'SEDAN'),
        ('coupe', 'COUPE'),
        ('sports', 'SPORTS CAR'),
        ('stationwagon', 'STATION WAGON'),
        ('hatchback', 'HATCHBACK'),
        ('convertible', 'CONVERTIBLE'),
        ('suv', 'SPORT-UTILITY VEHICLE (SUV)'),
        ('minivan', 'MINIVAN'),
        ('pickup', ' PICKUP TRUCK'),
    ]
    variant = forms.ChoiceField(choices=VARIANT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    year = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter year vehicle was bought'}))
    kilometer = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter kilometers vehicle travelled'}))
    regno = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your vehicle registration id'}))
    expectedprice = forms.CharField(max_length= 10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter expected price (in number)'}))
    DEALER_STATE_CHOICES = [
        ('', 'SELECT STATE'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Orissa', 'Orissa'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttaranchal', 'Uttaranchal'),
        ('West Bengal', 'West Bengal'),
    ]
    dealer_state = forms.ChoiceField(choices=DEALER_STATE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    DEALER_CITY_CHOICES = [
        ('', 'SELECT CITY'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Chandigarh', 'Chandigarh'),
        ('Coimbatore', 'Coimbatore'),
        ('Gurgaon', 'Gurgaon'),
        ('Hyderabad', 'Hyderabad'),
        ('Jaipur', 'Jaipur'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Noida', 'Noida'),
        ('Thane', 'Thane'),
        ('Patna', 'Patna'),
        ('Pune', 'Pune'),
    ]
    dealer_city = forms.ChoiceField(choices=DEALER_CITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    DEALER_CHOICES = [
        ('', 'SELECT DEALER'),
        ('1', 'DEALER A'),
        ('2', 'DEALER B'),
        ('3', 'DEALER C'),
        ('4', 'DEALER D'),
        ('5', 'DEALER E'),
    ]
    dealer = forms.ChoiceField(choices=DEALER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = SellCar
        fields = [
            'fullname',
            'email',
            'state',
            'city',
            'make',
            'name',
            'variant',
            'year',
            'kilometer',
            'regno',
            'expectedprice',
            'dealer_state',
            'dealer_city',
            'dealer',
        ]

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if len(fullname) < 3:
            raise forms.ValidationError("Name cannot be less than 3 characters")
        return fullname

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Email should end with @gmail.com")
        account = False
        for instance in User.objects.all():
            if instance.email == email:
                account = True
                break
        if not account:
            raise forms.ValidationError("An account doesn't exist with the given email")
        return email

    def clean_otp(self):
        otp = self.cleaned_data.get('otp')
        if not otp.isalnum():
            raise forms.ValidationError('OTP generated is alphanumeric')
        if not otp:
            raise forms.ValidationError('OTP Verification is required!')
        if len(otp)!=6:
            raise forms.ValidationError('OTP is 6 character long!')

    def clean_year(self):
        year = int(self.cleaned_data.get('year'))
        if len(str(year))!=4 or year<0:
            raise forms.ValidationError("Year is invalid")
        return year

    def clean_kilometer(self):
        kilometer = float(self.cleaned_data.get('kilometer'))
        if kilometer<0:
            raise forms.ValidationError("Length cannot be negative")
        return kilometer

    def clean_regno(self):
        regno = int(self.cleaned_data.get('regno'))
        if len(str(regno)) < 5:
            raise forms.ValidationError("Cannot be less than 5 digits")
        if regno<0:
            raise forms.ValidationError("Registration number cannot be negative")
        return regno

    def clean_expectedprice(self):
        expectedprice = float(self.cleaned_data.get('expectedprice'))
        if len(str(expectedprice)) < 5:
            raise forms.ValidationError("Cannot be less than 5 digits")
        if expectedprice<0:
            raise forms.ValidationError("Price cannot be negative")
        return expectedprice