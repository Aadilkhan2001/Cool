from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from myapp.models import CustomerModel

class UserCForm(UserCreationForm):
    password1=forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=PasswordInput(attrs={'class':'form-control','placeholder':'confirm Password'}))

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Lastname'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}),
        }

class LogInForm(AuthenticationForm):
     username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
     password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))

     class Meta:
         model=User
         fields=['username','password']

class UserProfileChangeForm(UserChangeForm):
    password=None
    class Meta:
         model=User
         fields=['username','first_name','last_name','email']

         widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'})
    }

class ChangePassForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter old Password'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter old Password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter old Password'}))

    class Meta:
        model=User
        fields=['old_password','new_password1','new_password2']

class PassReset(PasswordResetForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter E-Mail'}))

class PassSet(SetPasswordForm):
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter New Password'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))

co=(('India','India'),)
city=(('Ahemdabad','Ahemdabad'),)
state=(('Gujrat','Gujrat'),)
class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields = [ "zip_code", "state", "city", "add2", "add1", "country", "cc_add", "ccname", "mobile", "email", "last_name", "first_name"][::-1]
        widgets = {
                "first_name":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter First Name'}),
                "last_name":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter Last Name'}),
                "email":forms.EmailInput(attrs={'class':'form-control text-center','placeholder':'Enter E-mail'}),
                "mobile":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter Mobile Number'}),
                "ccname":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter Company Name'}),
                "cc_add":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter Company Address'}),
                "add2":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'House Number & Street name (Optional)'}),
                "add1":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Apartment, Suite, Unit etc. (Optional)'}),
                "country":forms.Select(attrs={'class':'form-control text-center','class':'country-select form-control text-center'},choices=co),
                "city":forms.Select(attrs={'class':'country-select form-control text-center'},choices=city),
                "state":forms.Select(attrs={'class':'country-select form-control text-center'},choices=state),
                "zip_code":forms.TextInput(attrs={'class':'form-control text-center','placeholder':'Enter Zipcode'}),
        }