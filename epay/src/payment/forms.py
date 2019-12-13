from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
# from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.contrib.auth import get_user_model
from payments import get_payment_model
from . import models


class PaymentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(Field('currency',))

    class Meta:
        model = models.Payment
        fields = ['currency', ]
