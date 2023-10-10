from rest_framework import serializers
from .models import *

class BUPA_DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BUPA_Data
        exclude = ['id']



class HeartDiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartDisease
        exclude = ['id']


class ChronicKidneyPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChronicKidneyPrediction
        exclude = ['id']

class DiabeticsPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabeticsPrediction
        exclude = ['id']
