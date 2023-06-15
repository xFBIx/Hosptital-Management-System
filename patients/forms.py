from django import forms
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
GENDER_CHOICES =(
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)
class profileform(forms.Form):
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required=True)
    history_of_illness = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    record_of_prescriptions = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}))
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['history_of_illness', 'record_of_prescriptions']