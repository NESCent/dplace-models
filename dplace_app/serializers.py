from rest_framework.relations import RelatedField
from rest_framework_gis import serializers as gis_serializers
from models import *
from rest_framework import serializers

class EAVariableCodeDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = EAVariableCodeDescription
		fields = ('id', 'code', 'description', 'variable')

class EAVariableDescriptionSerializer(serializers.ModelSerializer):
	class Meta:
		model = EAVariableDescription
		fields = ('id', 'number', 'name')

class SocietySerializer(gis_serializers.GeoModelSerializer):
	class Meta:
		model = Society
		fields = ('id', 'ext_id', 'name', 'location', 'iso_code', 'source')

class EAVariableValueSerializer(serializers.ModelSerializer):
	variable = serializers.IntegerField(source='code.variable_id')
	variable_name = serializers.CharField(source='code.variable.name')
	code_value = serializers.CharField(source='code.code')
	code_description = serializers.CharField(source='code.description')
	class Meta:
		model = EAVariableValue
		fields = ('id', 'society', 'code', 'variable','variable_name', 'code_value', 'code_description')

class ISOCodeSerializer(gis_serializers.GeoModelSerializer):
	class Meta:
		model = ISOCode

class EnvironmentalSerializer(gis_serializers.GeoModelSerializer):
	class Meta:
		model = Environmental