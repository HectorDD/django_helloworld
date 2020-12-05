from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializador basico'''
    name = serializers.CharField(max_length=10)
    