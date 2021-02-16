from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Attribute, UseCase

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UseCaseForm(forms.ModelForm):
    name = forms.CharField(label='Name of the Use Case:')

    class Meta:
        model = UseCase
        fields = ['name',]

class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields= ()
    
    def __init__(self, *args, **kwargs):
        super(AttributeValueForm,self).__init__(*args,**kwargs)
        #self.attribute=False

    def get_all_attributes(self):
        all_attributes = Attribute.objects.all()
        return all_attributes
        



