from django import forms


class CheckoutForm(forms.Form):
    client = forms.CharField(label='Your name', max_length=255)
