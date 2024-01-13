from django import forms
from .models import SignUP


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUP
        fields = ['email', 'full_name']

    def clean_email(self):
        # print(self.cleaned_data)
        # return "baddikati@yahoo.com"
        email = self.cleaned_data.get('email')
        # if not "gov" in email:
        #     raise forms.ValidationError(" Please, enter .gov domain ")
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == "gov"  :
            raise forms.ValidationError(" Please, enter .gov domain ")
        if not "erbil" in domain:
            raise forms.ValidationError(" Please, make sur using erbil domain")
        return email


    def clean_full_name(self):

        full_name = self.cleaned_data.get('full_name')
        #if
        return full_name


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email     = forms.EmailField(required=False)
    message   = forms.CharField(required=False)
