from django import forms
from dragon_ball.models import Dragonball, Dragonballsaga, Dragonballvivo, User




class dragonballForm(forms.ModelForm):

    class Meta:
        model = Dragonball
        fields = [
            'name',
            'ki',
            'raza',
            'años',
        ]

class dragonballsagaForm(forms.ModelForm):
    class Meta:
        model = Dragonballsaga
        fields = [
            'name',
            'saga',
            'capitulos',
            'villano',
            'transformaciones',
        ]

class dragonballvivoForm(forms.ModelForm):
    class Meta:
        model = Dragonballvivo
        fields = [
            'name',
            'vivo',
        ]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'dragonballs',
            'dragonballsagas',
            'dragonballvivos',
        ]