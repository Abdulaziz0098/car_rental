from django.forms import ModelForm

from company.models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        exclude = ['customer', 'car', 'total_day']
