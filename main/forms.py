from django import forms

from .models import AdvUser

class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес электронной почты', required=True)


    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')
