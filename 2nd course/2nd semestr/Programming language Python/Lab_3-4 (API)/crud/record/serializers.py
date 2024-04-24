from rest_framework import serializers
from .models import Records

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = '__all__'

    def create(self, validated_data):
        return Records.objects.create(**validated_data)
