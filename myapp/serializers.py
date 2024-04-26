# myapp/serializers.py
from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    data = serializers.CharField(max_length=100)
