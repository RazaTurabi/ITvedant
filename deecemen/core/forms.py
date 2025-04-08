from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomerDetails, Subscription

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        

class CustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        fields = ['name', 'address', 'phone', 'state', 'city', 'pincode']
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
                  'address':forms.TextInput(attrs={'class':'form-control'}),
                  'phone':forms.TextInput(attrs={'class':'form-control'}),
                  'state':forms.TextInput(attrs={'class':'form-control'}),
                  'city':forms.TextInput(attrs={'class':'form-control'}),
                  'pincode':forms.NumberInput(attrs={'class':'form-control'}),
                  }
        
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']