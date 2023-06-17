from django import forms
from django.contrib.auth.forms import UserCreationForm
from Doctor.models import CustomUser

class ContactForm(forms.Form):
    name=forms.CharField(max_length=255)
    title=forms.CharField(max_length=255)
    email=forms.EmailField()
    content=forms.CharField(widget=forms.Textarea)




class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username-field' , 'placeholder': 'username'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'name-field' , 'placeholder': 'name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password1-field' ,'placeholder': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password2-field' , 'placeholder': 'confirm password'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone-number-field' , 'placeholder': 'phone number'}))
    specialization = forms.CharField(widget=forms.TextInput(attrs={'class': 'specialization-field' , 'placeholder': 'specialization'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class': 'country-field' , 'placeholder': 'country'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'email-field' , 'placeholder': 'email'}))
    license_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'license-number-field' , 'placeholder': 'license number'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'password1', 'password2', 'phone_number', 'specialization', 'country', 'email', 'license_number')



from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'username-field', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-field', 'placeholder': 'password'}))


