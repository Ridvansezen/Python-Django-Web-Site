from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=25,min_length=2,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(max_length=25,min_length=2,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))