from django.contrib.auth.forms import AuthenticationForm , UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


attrs= {'class':'form-control'}

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username=forms.CharField(
        label= 'Username',
        widget=forms.TextInput(attrs=attrs)
    )
    password=forms.CharField(
        label= 'Password',
        widget=forms.PasswordInput(attrs=attrs)
    )

class UserRegisterForm(UserCreationForm):
    first_name= forms.CharField(
        label= 'First Name',
        widget= forms.TextInput(attrs=attrs)
    )
    last_name= forms.CharField(
        label= 'Last Name',
        widget= forms.TextInput(attrs=attrs)
    )
    username= forms.CharField(
        label= 'Username',
        widget= forms.TextInput(attrs=attrs)
    )
    email= forms.EmailField(
        label= 'Email',
        widget= forms.TextInput(attrs=attrs)
    )
    password1= forms.CharField(
        label= 'Password',
        widget= forms.PasswordInput(attrs=attrs),
        strip= False
    )
    password2= forms.CharField(
        label= 'Password Confirmation',
        widget= forms.PasswordInput(attrs=attrs),
        strip= False
    )
    class Meta(UserCreationForm.Meta):
        fields= ('first_name','last_name','username','email' )

class ProfileForm(UserChangeForm):
    first_name=forms.CharField(
        label="First Name",
        required=True,
        widget=forms.TextInput(attrs=attrs)
    )
    last_name=forms.CharField(
        label="Last Name",
        required=True,
        widget=forms.TextInput(attrs=attrs)
    )
    email=forms.CharField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs=attrs)
    )
    password = None
    class Meta:
        model= User
        fields= ('first_name',"last_name","email")
        widgets={
            'first_name':forms.TextInput(attrs=attrs),
            'last_name':forms.TextInput(attrs=attrs),
            'email':forms.EmailInput(attrs=attrs)
        
        }