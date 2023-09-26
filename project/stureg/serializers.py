from rest_framework import serializers
from stureg.models import Stureg

class SturegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stureg
        fields= ('id',
                 'sname',
                 'srollno',
                 'sdob',
                 'sbg',
                 'pgname',
                 'pgphno',
                 'pgmail')