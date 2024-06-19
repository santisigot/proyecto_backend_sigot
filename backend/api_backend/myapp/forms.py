from django import forms

from myapp.models import Funko, User




class FunkoForm(forms.ModelForm):

    class Meta:
        model = Funko
        fields = [
            'name',
            'number',
            'collection',
        ]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'funkos',
        ]