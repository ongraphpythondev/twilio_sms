from django import forms
from phonenumber_field.formfields import PhoneNumberField


class MessageForm(forms.Form):
    to = PhoneNumberField()
    body = forms.CharField(widget=forms.Textarea)
