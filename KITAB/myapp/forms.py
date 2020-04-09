from django import forms
from django.core import validators
from myapp.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password',)
        help_texts = {
            'username': None,
        }
        date_of_birth = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
        )
class UserDetForm(forms.ModelForm):
    class Meta():
        model = UserDet
        fields = ('dob','document',)
class UserProfileForm(forms.ModelForm):
    # uname = forms.CharField(widget=forms.HiddenInput()) #added
    class Meta():
        model = UserProfile
        exclude = ('user','modified_date','created_date',)

class UserEduDetailsForm(forms.ModelForm):
    # uname = forms.CharField(widget=forms.HiddenInput()) #added
    class Meta():
        model = UserEduDetails
        exclude = ('user','modified_date','created_date',)

class UserSkillDetailsForm(forms.ModelForm):
    # uname = forms.CharField(widget=forms.HiddenInput()) #added
    class Meta():
        model = UserSkillDetails
        exclude = ('user','modified_date','created_date',)
