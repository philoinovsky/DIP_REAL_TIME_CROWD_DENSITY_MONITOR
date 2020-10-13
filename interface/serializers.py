from rest_framework import serializers
from . models import s2_1,s2_b1,s2_b2,s2_b3,s2_b4

class s2_1_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = s2_1
        fields = ['id','name','capacity','occupied']

class s2_b1_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = s2_b1
        fields = ['id','name','capacity','occupied']

class s2_b2_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = s2_b2
        fields = ['id','name','capacity','occupied']

class s2_b3_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = s2_b3
        fields = ['id','name','capacity','occupied']

class s2_b4_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = s2_b4
        fields = ['id','name','capacity','occupied']