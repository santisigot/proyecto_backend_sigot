# dragon_ball/serializers.py

from rest_framework import serializers
from dragon_ball.models import Dragonball, Dragonballsaga, Dragonballvivo


class DragonballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragonball
        fields = ['name', 'ki', 'raza', 'años']

class DragonballsagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragonballsaga
        fields = ['name','saga', 'capitulos', 'villano', 'transformaciones']

class DragonballvivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dragonballvivo
        fields = ['name', 'vivo']
