from django import forms

from home.models import User, City
from models.models import Model, Variant

from .models import SellCar, ExchangeCar

class SellCarModelForm(forms.ModelForm):
    fullname = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                                         'placeholder':'Enter your email'}))

    year = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter year vehicle was bought'}))
    kilometer = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter kilometers vehicle travelled'}))
    regno = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your vehicle registration id'}))
    expectedprice = forms.CharField(max_length= 10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter expected price (in number)'}))

    class Meta:
        model = SellCar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['model'].queryset = Model.objects.none()
        self.fields['variant'].queryset = Variant.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

        if 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['model'].queryset = Model.objects.filter(make_id=make_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Model queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.make.model_set.order_by('name')

        if 'model' in self.data:
            try:
                model_id = int(self.data.get('model'))
                self.fields['variant'].queryset = Variant.objects.filter(model_id=model_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Variant queryset
        elif self.instance.pk:
            self.fields['variant'].queryset = self.instance.model.variant_set.order_by('name')

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
        for instance in SellCar.objects.all():
            if instance.regno == regno:
                raise forms.ValidationError('This car with regno '+str(regno)+' is already on sale!')
        return regno

    def clean_expectedprice(self):
        expectedprice = float(self.cleaned_data.get('expectedprice'))
        if len(str(expectedprice)) < 5:
            raise forms.ValidationError("Cannot be less than 5 digits")
        if expectedprice<0:
            raise forms.ValidationError("Price cannot be negative")
        return expectedprice

class ExchangeCarModelForm(forms.ModelForm):
    fullname = forms.CharField(max_length= 100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your full name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                                         'placeholder':'Enter your email'}))

    year = forms.CharField(max_length=4, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter year vehicle was bought'}))
    kilometer = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter kilometers vehicle travelled'}))
    regno = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter your vehicle registration id'}))
    expectedprice = forms.CharField(max_length= 10, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Enter expected price (in number)'}))

    class Meta:
        model = ExchangeCar
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
        self.fields['model'].queryset = Model.objects.none()
        self.fields['variant'].queryset = Variant.objects.none()
        # self.fields['dealercity'].queryset = City.objects.none()
        # self.fields['car_model'].queryset = Model.objects.none()
        # self.fields['car_variant'].queryset = Variant.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = City.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

        if 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['model'].queryset = Model.objects.filter(make_id=make_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Model queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.make.model_set.order_by('name')

        if 'model' in self.data:
            try:
                model_id = int(self.data.get('model'))
                self.fields['variant'].queryset = Variant.objects.filter(model_id=model_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Variant queryset
        elif self.instance.pk:
            self.fields['variant'].queryset = self.instance.model.variant_set.order_by('name')

        # if 'dealerstate' in self.data:
        #     try:
        #         dealerstate_id = int(self.data.get('dealerstate'))
        #         self.fields['city'].queryset = City.objects.filter(dealerstate_id=dealerstate_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['dealercity'].queryset = self.instance.dealerstate.city_set.order_by('name')
        #
        # if 'car_make' in self.data:
        #     try:
        #         car_make_id = int(self.data.get('car_make'))
        #         self.fields['car_model'].queryset = Model.objects.filter(car_make_id=car_make_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty Model queryset
        # elif self.instance.pk:
        #     self.fields['car_model'].queryset = self.instance.car_make.model_set.order_by('name')
        #
        # if 'car_model' in self.data:
        #     try:
        #         car_model_id = int(self.data.get('car_model'))
        #         self.fields['car_variant'].queryset = Variant.objects.filter(car_model_id=car_model_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty Variant queryset
        # elif self.instance.pk:
        #     self.fields['car_variant'].queryset = self.instance.car_model.variant_set.order_by('name')

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
        for instance in SellCar.objects.all():
            if instance.regno == regno:
                raise forms.ValidationError('This car with regno '+str(regno)+' is already on sale!')
        return regno
    
    def clean_expectedprice(self):
        expectedprice = float(self.cleaned_data.get('expectedprice'))
        if len(str(expectedprice)) < 5:
            raise forms.ValidationError("Cannot be less than 5 digits")
        if expectedprice<0:
            raise forms.ValidationError("Price cannot be negative")
        return expectedprice