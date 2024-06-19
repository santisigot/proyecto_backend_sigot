from rest_framework import serializers

from myapp.models import Funko


class FunkoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funko
        fields = ['name' , 'number', 'collection' ]
        

