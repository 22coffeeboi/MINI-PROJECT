from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Textarea
from django.template.defaulttags import comment

from .models import Persons, reg, admins


class NameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NameForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['pasn'].required = False

    class Meta:
        model = Persons
        fields = ('name', 'pasn')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'pasn': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
            }),

        }


class RegForm(forms.ModelForm):
    class Meta:
        model = reg
        fields = ('name', 'pasn1', 'pasn2', 'email')
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Username'
            }),
            'pasn1': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Password'
            }),
            'pasn2': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 're-type password'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'example@gmail.com'
            }),
        }


class admins(forms.ModelForm):
    class Meta:
        model = admins
        fields = ('adminname', 'roomnum', 'reso')
        labels = {
            "adminname": "",
            "roomnum": "",
            "reso": "",
        }
        widgets = {
            'adminname': TextInput(attrs={
                'class': "form__input",

                'style': 'max-width: 300px;',

                'placeholder': 'Username',
                'readonly': 'readonly'
            }),
            'roomnum': TextInput(attrs={
                'class': "form__input",
                'style': 'max-width: 300px;',

                'placeholder': 'Room No'
            }),
            'reso': Textarea(attrs={
                'class': "form__input",

                'placeholder': 'resources',
                'rows': 10,
                'cols': 30,
            }),

        }
