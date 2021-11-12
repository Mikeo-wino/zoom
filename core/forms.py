from django.forms import ModelForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['terms']

class ContentRequestForm(ModelForm):
    class Meta:
        model = ContentRequestModel
        fields = '__all__'
