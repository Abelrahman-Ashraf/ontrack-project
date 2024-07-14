from django import forms
from django.contrib.auth.models import User
from .models import profile,Shipment
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from django.core.validators import RegexValidator

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =('username', 'email' , 'password1' , 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})    
        



class Login_Form(forms.ModelForm):
    # username =forms.CharField()
    # password =forms.CharField()
    class Meta:
        model = User
        fields = ('username' , 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})    



class User_form(forms.ModelForm):
    username = forms.CharField()
    class Meta:
        model = User 
        fields =('username','email')        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class Profile_form(forms.ModelForm):
    
    class Meta:
        model = profile
        fields =('name' ,'phone' ,'location')        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})   


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = (
            'shipment_id',
            'shipment_type',
            'shipment_weight',
            'receiver_name',
            'sender_name',
            'sender_phone',
            'receiver_phone',
            'start_location',
            'last_location',
            'about_shipment',
            'received_date',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['received_date'].widget = DateInput(attrs={'type': 'date'})
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})    